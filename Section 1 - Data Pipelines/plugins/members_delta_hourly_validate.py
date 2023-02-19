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

class MembersDeltaHourlyValidateOperator(BaseOperator):
    @apply_defaults
    def __init__(
        self,
        file_path,
        *args, **kwargs):
        super(MembersDeltaHourlyValidateOperator, self).__init__(*args, **kwargs)

        self.file_path = file_path
        self.df = pd.DataFrame()

    # function to read csv files from designed filepath
    def _load_files(self, context, execution_time):
        sucess_file = self.file_path + 'success/members' + '_' + execution_time + '.csv'
        if os.path.exists(sucess_file):
            self.df = pd.read_csv(sucess_file)
            logging.info('There are files to validate')
        else:
            logging.info('There are no files to validate')
            return

    def _validate(self, context, execution_time):

        # defines several regular expressions that will be used later to check the validity of certain fields in the data.
        pat=r'(\,|\.|Mrs|Jr|Dr|Mr|MD|DDS|DVM|PhD|III|II|Miss|Ms)'
        special_characters = "!@#$%^&*()-+?_=,<>/"

        # function to check if name is valid
        def _validate_name(text):
            if bool(re.search(pat, text)) or any(c in special_characters for c in text):
                raise ValueError('There are invalid characters in name')
            else:
                # logging.info('Name Validation Passed')
                return

        # function to check if date of birth is of valid format
        def _validate_date(text):
            if len(str(text)) != 8 or bool(datetime.strptime(str(text), '%Y%m%d').strftime('%Y-%m-%d')) == False:
                raise ValueError('There are invalid Date of Birth')
            else:
                # logging.info('Date of Birth Validation Passed')
                return

        # function to check if email is of valid format
        def _validate_email(text):
            if text.endswith('.com') or text.endswith('.net'):
                # logging.info('Email Validation Passed')
                return
            else:
                raise ValueError('There are invalid Emails')

        logging.info('Start Validating Data')

        # This section takes the CSV files, cleans and validates data, generates a membership ID for valid data, and saves successful and failed into sucess and failed folder respectively.
        if len(self.df) >= 1:
            df = self.df 
        else:
            logging.info('There are no files to validate. Exiting')
            return

        # Reset the index of the dataframe.
        df = df.reset_index()

        # validate the first name and last name column
        df['first_name'].apply(lambda x: _validate_name(x))
        df['last_name'].apply(lambda x: _validate_name(x))

        # validate the email column
        df['email'].apply(lambda x: _validate_email(x))

        # validate the date_of_birth column
        df['date_of_birth'].apply(lambda x: _validate_date(x))

        # validate users are above 18
        if len(df[df['above_18']==False]) > 0:
            raise ValueError('There are users below 18')
        
        logging.info('All validation checks have passed')

    # function to execute operator
    def execute(self, context):
        execution_date = context.get('execution_date')
        execution_time= context.get('ts')
        self._load_files(context, execution_time)
        self._validate(context, execution_time)

