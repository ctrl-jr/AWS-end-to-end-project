import awswrangler as awr
import pandas as pd


def lambda_handler(event, context):
    # Get the object from the event and show its content type
    #bucket = event['Records'][0]['s3']['bucket']['name']
    #key = urllib.parse.unquote_plus(event['Records'][0]['s3']['object']['key'], encoding='utf-8')
    try:

        # Create df from the json file in our S3 bucket
        df_json = awr.s3.read_json('s3://jr-s3-001/game-list.json')

        # Convert JSON to parquet
        awr_response = awr.s3.to_parquet(
            df=df_json,
            path='s3://jr-s3-clean-data/game-list.parquet',
            dataset=True,
            database='glue-db-0O1',
            table='jr_s3_001',
        )

        return awr_response
    except Exception as e:
        print(e)
        print('Error getting object from bucket. Make sure they exist and your bucket is in the same region as this function.')
        raise e