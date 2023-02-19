# Section 4 - Charts and APIs

This section of the repository contains the resources and code to extract, clean, and visualize data from https://covid19api.com/ as instructed. Looker Studio (Google Cloud Data Studio) was used as the visualization tool.

There are several assumptions made which is currently listed:
1. Covid Data is extracted and refreshed on a fixed interval. A CSV file is used here as a local development test. In actual production, data may be loaded into a Data Warehouse.
2. Schema of Covid data is consistent

# Dashboard Link

Here is the link to the dashboard - https://lookerstudio.google.com/reporting/a759b87a-b24b-4bfd-adf0-19cedb625cfa

# Project Walkthrough

1. Covid Data was extracted through the API using singapore_covid_extract.py which outputs a CSV file into the resources folder.
2. CSV file is then imported into Looker Studio and visualized.

# Files and Folder Structure
- resources: Contains the CSV file output from https://covid19api.com/ 
- video: Contains a .mov file to demonstrated the capabilities and functionalities of the visualization
- screenshot: Contains a .png file to demonstrate the outlook of the dashboard
- link: a link to the dashboard is provided

# Extra
Picture to visualize the Dashboard.


![Diagram to visualize Pipeline Logic](Data-Engineer-Tech-Challenge-Singapore-Covid-Data.png?raw=true "Singapore Covid Cases")
