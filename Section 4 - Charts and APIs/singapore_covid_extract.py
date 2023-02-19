# import libraries
import requests
import pandas as pd
from dateutil import parser
from datetime import datetime

# define a function to parse date
def _parse_date(text):
    date = parser.isoparse(text)
    date = date.strftime('%Y-%m-%d')
    return date

# generate a dataframe to hold all covid data
df_total = pd.DataFrame()

# generate a loop to get confirmed, recovered and deaths data from API
for i in ['confirmed','recovered','deaths']:
	# Make an HTTP GET request to the API endpoint
    response = requests.get('https://api.covid19api.com/dayone/country/singapore/status/'+ i)

    # Parse the JSON data from the response into a Python object
    data = response.json()

    # Import JSON data into dafaframe, parse date and calculate new cases and growth rate
    df = pd.DataFrame(data)
    df['date_cleaned']=df['Date'].apply(lambda x: _parse_date(x))
    df['new_cases'] = df['Cases'].diff()
    df['growth_rate'] = df['new_cases']/df['Cases']
    df = df[['Country','Cases','Status','date_cleaned','new_cases','growth_rate']]
    df = df.fillna(0)

    # append current data to df_total
    df_total = df_total.append(df)

# output all covid data containing confirmed, recovered, and deaths to resources
df_total.to_csv('resources/20230219-singapore-covid-cases.csv',index=False)