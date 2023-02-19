# This is a Python script that defines an Airflow DAG (Directed Acyclic Graph) for a data extraction process.
# Import necessary modules:
from airflow.exceptions import AirflowException
from airflow import models
from airflow import DAG
from members_delta_hourly_extract import MembersDeltaHourlyExtractOperator
from datetime import datetime, timedelta
import os

# Define schedule interval DAG (in cron notation) and file path for the CSV files
schedule_interval_dag = '0 * * * *'
file_path_dag = '/opt/airflow/dags/members_delta_extract_hourly_dag/resources/'

# Define a function that will be used to send email alerts if the DAG fails.
def notify_email(contextDict, **kwargs):
    """Send custom email alerts."""

    # email title.
    title = "Airflow ERROR : {dag} Failed".format(**contextDict)

    # email contents
    body = """
    IMPORTANT, <br>
    <br>
    There's been an error in the {dag} job.<br>
    <br>
    Airflow bot <br>
    """.format(**contextDict)

    send_email('nickmydata@gmail.com', title, body)

# Define default arguments for the DAG, including the start date, whether the DAG should depend on past executions, email settings, project ID, number of retries, and retry delay.
default_dag_args = {
 'start_date': datetime(2023, 2, 18),
 'depends_on_past': True,
 'email_on_failure': True,
 'email_on_retry': True,
 'project_id' : 'mudah-analytics-222509',
 'on_failure_callback': notify_email,
 'retries': 1,
 'retry_delay': timedelta(minutes=5),
}

# Create a DAG object, passing in the DAG ID, schedule interval, catchup flag, and default arguments.
with models.DAG(
 dag_id='members_delta_hourly_extract',
 schedule_interval = schedule_interval_dag,
 catchup = True,
 default_args=default_dag_args) as dag:

 # Define a task for the DAG, which uses a custom operator (MembersDeltaHourlyExtractOperator) to perform the data cleansing and loading. 
 # The task ID and file path are passed as arguments to the operator. The last line just adds the task to the DAG.

 clean_and_load=MembersDeltaHourlyExtractOperator(
 task_id='clean_and_load',
 file_path= file_path_dag)

 clean_and_load