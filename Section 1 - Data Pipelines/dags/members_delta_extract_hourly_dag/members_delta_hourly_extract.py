# This is a Python script that defines an Airflow DAG (Directed Acyclic Graph) for a data extraction process.
# Import necessary modules:
from airflow.exceptions import AirflowException
from airflow import models
from airflow import DAG
from members_delta_hourly_extract import MembersDeltaHourlyExtractOperator
from members_delta_hourly_validate import MembersDeltaHourlyValidateOperator
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
 'start_date': datetime.now() - timedelta(hours = 2),
 'depends_on_past': False,
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

 # Define tasks for the DAG, which uses a custom operators to perform cleaning, loading, and validating 
 # The task ID and file path are passed as arguments to the operator. The last line adds sequencial dependency to the dag

 clean_and_load=MembersDeltaHourlyExtractOperator(
 task_id='clean_and_load_task',
 file_path= file_path_dag)

 validate=MembersDeltaHourlyValidateOperator(
 task_id='validate_task',
 file_path= file_path_dag)

 clean_and_load >> validate