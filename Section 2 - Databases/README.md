# Section 2 - Databases
This section of the repository contains the resources and SQL code to initialize a postgres database containing the tables which correlates to the entities of the requirement. DBeaver was used as a DB visualization tool.

Assumptions:

1.member_id is the same as membership_id

# Install and Run the project

1. Run the bash commands in init.sh
2. Execute the DML.sql file in the postgres database
3. Run resources/sample_queries.sql to validate results

# Files and Folder Structure

* Dockerfile: Dockerfile required to build docker image
* DDL.sql: SQL init for docker-entrypoint-initdb.d/ which creates required tables
* DML.sql: SQL Insert Statement to generate mock data 
* resources: Contains sample_queries.sql to answer the assignment requirements
* .png files: Screenshot and diagram to visualize database

# Entity-Relationship Diagram

![Entity-Relationship Diagram](section-2-erd-diagram.png?raw=true "Entity-Relationship Diagram")

* Transactions: The Entity-Relationship is designed with transactions as the fact table. Each transaction can have multiple records if there are different items bought in that transaction. The composite primary key for the transactions table is transaction_id and item_id, which states that for each item, there can only be 1 record for each transaction. The quantity, total_price, and total_weight is also displayed for that item. Lastly, the transaction_datetime and member_id is also recorded for each transaction

* members: The members table is a dimension table containing information for each member. In this particular case, we had generated data based on the output from section 1, which gives us the first and last name, email, and phone number of the member. The member_id is the primary key for this table. Members table has a mandatory one to many optional relationship with the transactions table.

* items: The items table is a dimension table containing information for each item. There are information such as item name, manufacture name, weight of the item, and its cost. The item_id is the primary key for this table. Items table has a mandatory one to many optional relationship with the transactions table.

# Results
The query to produce results for the following requirements:
1. Which are the top 10 members by spending
2. Which are the top 3 items that are frequently brought by members
can be found in the resources folder

# Extra

Screenshot of Postgres Database and Transactions table

![Database Query](database-query-view.png?raw=true "Database Query")

