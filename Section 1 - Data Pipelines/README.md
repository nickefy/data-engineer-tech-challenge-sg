# Section 1 - Data Pipeline

This section of the repository contains the resources and code to clean, load, and validate the CSV files provided.
Airflow was used as the workflow management system.

There are several assumptions made which is currently listed:
1. CSV files are dropped in a cloud storage with proper naming formats
2. Schema of CSV files are consistent

# Install and Run the Project 

1. Install Docker as per instructions here - https://docs.docker.com/engine/install/
2. Run Airflow as per instructions here - https://airflow.apache.org/docs/apache-airflow/stable/howto/docker-compose/index.html or run it via the bash file init.sh
3. Overwrite the DAG and Plugins folder on Airflow with the resources on the repository

# Files and Folder Structure
- dags: Contains the DAG, original CSV files, processed CSV files
- plugins: Contains the Operator logic to process and validate CSV files
- logs: Contains log of the the run

# Extra
Diagram to visualize Pipeline Logic.


![Diagram to visualize Pipeline Logic](section-1-data-pipeline.png?raw=true "Data Pipeline Logic")

Diagram to visualize pipeline on Airflow

![Diagram to visualize pipeline on Airflow](section-1-data-pipeline-airflow.png?raw=true "Diagram to visualize pipeline on Airflow")


* Successfully processed records can be found in dags/members_delta_extract_hourly_dag/resources/success/
* Failed records can be found in dags/members_delta_extract_hourly_dag/resources/failed/ - The records are formatted so that analysts can easily investigate why did the records fail
* Original CSV files that were processed can be found in dags/members_delta_extract_hourly_dag/resources/archive/