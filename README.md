# AWS End to End project

## Architecture
![image](https://github.com/ctrl-jr/AWS-end-to-end-project/assets/36134747/aed9c0bd-7fcc-4279-9e16-ae79db621a5c)

## Overview
This is a small project I did to get a better grasp in a few AWS services used in Data Engineering.

We start by extracting the top games 11 from Open Critic using a **Zillow API** into a **pandas dataframe**, which is then joined with a JSON containing their genre and publisher.   
Afterwards we upload the JSON to a **S3 bucket** that triggers a **Lambda function** to convert this JSON into Parquet and put it in another **S3 bucket**, next we run a **Glue Crawler** to get the data schema, make the appropriate changes (such as fixing **releaseDate** to date format), move this into **Data Catalog** and finally load the data in a **Serverless Redshift Cluster** for analysis.

## Tools
### Dataset (API)
- Zillow API

### Language 
- Python

### AWS Services
- **Lambda**: uses a trigger to detect when a file is uploaded to the first S3 bucket, then converts it into parquet format and sends it to the second S3 bucket.
- **S3 Buckets**: for storing our JSON and Parquet files.
- **Glue Crawler**: for discovering the metadata of the file in the S3 bucket which can be used to query the file.
- **Serverles Redshit**: data warehouse which allows us to store our games list and query it using SQL.
