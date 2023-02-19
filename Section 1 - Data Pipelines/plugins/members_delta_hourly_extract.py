import os
from airflow.models import BaseOperator, Variable
from airflow.utils.decorators import apply_defaults
import logging
import pandas as pd
import pendulum
import logging
from dateutil.parser import parse
from datetime import date
from datetime import datetime
import re
from hashlib import sha256

class MembersDeltaHourlyExtractOperator(BaseOperator):
    @apply_defaults
    def __init__(
        self,
        file_path,
        *args, **kwargs):
        super(MembersDeltaHourlyExtractOperator, self).__init__(*args, **kwargs)

        self.file_path = file_path
        self.df = pd.DataFrame()

    # function to read csv files from designed filepath
    def _load_files(self, context):
        _files = os.listdir(self.file_path)

        for file in _files:
            abs_path = '{}{}'.format(self.file_path, file)
            if abs_path.endswith('.csv'):
                _tmp_df = pd.read_csv(abs_path)
                self.df = self.df.append(_tmp_df)

    # function to archive csv files after processing
    def _archive_files(self, context):
        _files = os.listdir(self.file_path)
        file_path_archive = self.file_path + 'archive/'

        for file in _files:
            abs_path = '{}{}'.format(self.file_path,file)
            new_path = '{}{}'.format(file_path_archive,file)
            if abs_path.endswith('.csv'):
                os.rename(abs_path, new_path)


    def _clean_and_load(self, context, execution_time):

        # defines several regular expressions that will be used later to check the validity of certain fields in the data.
        regex_email = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.(com|net)\b'
        matches = ["02/31", "31/02", "02/30","30/02","02-31","31-02","30-02","02-30"]
        regex_phone = r'^[0-9]*$'
        pat=r'(\,|\.|Mrs|Jr|Dr|Mr|MD|DDS|DVM|PhD|III|II|Miss|Ms)'

        # function to check if name is valid
        def _check_valid_name(text):
            if text:
                if text == '':
                    return False
                else:
                    return True
            else: 
                return False

        # function to check if date is valid
        def _check_valid_date(text):
            if any([x in text for x in matches]):
                return False
            else:
                return True

        # function to check if email is valid
        def _check_valid_email(text):
            if(re.fullmatch(regex_email, text)):
                return True
            else:
                return False

        # function to check if phone is valid
        def _check_valid_phone(text):
            if(re.fullmatch(regex_phone, text)) and len(text) == 8:
                return True
            else:
                return False

        # function to parse date accordingly
        def _try_parsing_date(text):
            for fmt in ('%Y-%m-%d', '%d/%m/%Y', '%Y/%m/%d','%d-%m-%Y'):
                try:
                    return datetime.strptime(text, fmt)
                except ValueError:
                    for fmt2 in ('%m-%d-%Y','%m/%d/%Y'):
                        try:
                            return datetime.strptime(text, fmt2)
                        except ValueError:
                            pass
                    pass
            raise ValueError('no valid date format found')

        # function to remove prefix and suffixes of names
        def _try_cleaning_name(column):
            column.replace(pat,'',regex=True,inplace=True)
            return column

        # function to remove spaces in phone number
        def _try_cleaning_phone(text):
            text= text.replace(" ", "")
            return text

        # function to check if the member's age is above 18 
        def _check_above_18(born):
            today = date(2022, 1, 1)
            age = today.year - born.year - ((today.month, today.day) < (born.month, born.day))
            if age >= 18:
                return True
            else:
                return False

        # function to format birthday to yyyymmdd
        def _format_birthday(date):
            date = date.strftime("%Y%m%d")
            return date

        # function to generate membership id
        def _gen_membership_id(date,lastname):
            birthdate_hashed = sha256(date.encode('utf-8')).hexdigest()[0:5]
            membership_id = lastname + '_' + birthdate_hashed
            return membership_id

        # function to ensure no records were missed during the process
        def test_count_equal(df, df1, df2):
            if len(df1) + len(df2) != len(df):
                raise ValueError('records missed')
            else:
                logging.info('no records were missed during the cleaning process')
                return True
    

        logging.info('Start Cleaning and loading Data')


        # This section takes the CSV files, cleans and validates data, generates a membership ID for valid data, and saves successful and failed into sucess and failed folder respectively.
        df = self.df 

        # check if there are data to be processed
        if len(df) >= 1:
            logging.info('There are files to be processed')
        else:
            logging.info('There are no files to be processed')
            return

        # Reset the index of the dataframe.
        df = df.reset_index()

        # Create new columns in the dataframe for whether date of birth and email are valid.
        df['is_valid_date'] = df['date_of_birth'].apply(lambda x: _check_valid_date(x))
        df['is_valid_email'] = df['email'].apply(lambda x: _check_valid_email(x))

        # Create a new column in the dataframe for the cleaned date of birth, for valid dates only.
        df['date_of_birth_cleaned'] = df[df['is_valid_date']== True]['date_of_birth'].apply(lambda x: _try_parsing_date(x))

        # Modify the 'name' column and create a new column for whether the name is valid.
        df['name'] = _try_cleaning_name(df['name'])
        df['is_valid_name'] = df['name'].apply(lambda x: _check_valid_name(x))

        # Create a new column for the cleaned mobile number and for whether it is valid.
        df['mobile_no_cleaned'] = df['mobile_no'].apply(lambda x: _try_cleaning_phone(x))
        df['is_valid_phone'] = df['mobile_no_cleaned'].apply(lambda x: _check_valid_phone(x))

        # Create a new column for whether the person is above 18 years of age.
        df['above_18'] = df['date_of_birth_cleaned'].apply(lambda x: _check_above_18(x))

        # create a separate dataset for only the rows that have valid data for all the columns created above.
        sucessful = df[(df['is_valid_date'] == True) & (df['is_valid_email'] == True) & (df['is_valid_name'] == True) & (df['is_valid_phone'] == True) & (df['above_18'] == True)]

        # Select the rows that have invalid data for any of the columns created above, and select specific columns for these rows
        failed = df[(df['is_valid_date'] == False) | (df['is_valid_email'] == False) | (df['is_valid_name'] == False) | (df['is_valid_phone'] == False) | (df['above_18'] == False)]
        failed = failed[['name','email','date_of_birth','mobile_no','is_valid_date','is_valid_email','is_valid_name','is_valid_phone','above_18']]

        # Split the 'name' column into first name and last name columns, only for rows with valid data.
        sucessful[['first_name','last_name']] = sucessful['name'].loc[sucessful['name'].str.split().str.len() == 2].str.split(expand=True)

        # Format the date of birth column for valid rows.
        sucessful['date_of_birth'] = sucessful['date_of_birth_cleaned'].apply(lambda x: _format_birthday(x))

        # Generate a membership ID for each valid row, based on the last name and date of birth. 
        sucessful['membership_id'] = sucessful.apply(lambda x: _gen_membership_id(x['date_of_birth'],x['last_name']), axis=1)

        # Select only the desired columns for the successful data, and save to a CSV file with a name that includes the execution time.
        sucessful = sucessful[['first_name','last_name','date_of_birth','email','above_18','membership_id']]
        sucessful.to_csv(self.file_path + 'success/members' + '_' + execution_time + '.csv', index =False)

        # Output the failed records into the failed patch that includes the execution time
        failed.to_csv(self.file_path + 'failed/members' + '_' + execution_time  +'.csv', index =False)

        # To test if records were missed during the process
        test_count_equal(df, sucessful, failed)

        logging.info('Cleaning has completed and files have been output into sucess and failed folder respectively')
        logging.info('Sucessful records are output to ' + self.file_path + 'success/members' + '_' + execution_time + '.csv')
        logging.info('Failed records are output to ' + self.file_path + 'failed/members' + '_' + execution_time + '.csv')

    # function to execute operator
    def execute(self, context):
        execution_date = context.get('execution_date')
        execution_time= context.get('ts')
        self._load_files(context)
        self._clean_and_load(context, execution_time)
        self._archive_files(context)

