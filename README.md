# AWS End to End project

## Architecture
![image](https://github.com/ctrl-jr/AWS-end-to-end-project/assets/36134747/5d7f88d9-0cd9-4d88-8b21-d8a5ec9c2f18)



## Overview
This is a small project I did to get a better grasp in a few AWS services used in Data Engineering.

We start by extracting the top games 11 from Open Critic using a **Zillow API** into a **pandas dataframe**, dropping unnecesary columns and adding a new column which adds a label based on the game score, then we join it with a JSON containing their genre and publisher.   
Afterwards we upload the JSON to a **S3 bucket** that triggers a **Lambda function** to convert this JSON into Parquet and sends it to another **S3 bucket**, next we run a **Glue Crawler** to examine our file and produces a table with the data schema so we  make the appropriate changes (such as changing **releaseDate** to date format), then we create a  **Redshift** connection so we can finally load the data in a **Serverless Redshift Cluster** for analysis.

## Tools
### Dataset (API)
- [Rapid API](https://rapidapi.com/opencritic-opencritic-default/api/opencritic-api)

### Language 
- Python

### AWS Services
- **Lambda**: uses a trigger to detect when a file is uploaded to the first S3 bucket, then converts it into parquet format and sends it to the second S3 bucket.
- **S3 Buckets**: for storing our JSON and Parquet files.
- **Glue**: for discovering the metadata of the file in the S3 bucket, creates a table with the schema which can be used to query our data.
- **Redshit Serverless**: data warehouse that allows us to store our games list and analyze it using SQL.
