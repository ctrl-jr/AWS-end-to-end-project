import awswrangler as awr
import pandas as pd


def lambda_handler(event, context):
    try:

        # Create df from the json file in our S3 bucket
        df_json = awr.s3.read_json('s3://jr-s3-001/game-list.json')

        # Dropping columns we don't need
        df1 = df_json.drop(columns=['tier', 'id', 'images.box.og', 'images.box.sm', 'images.banner.og', 'images.banner.sm'])

        # Convert JSON to parquet
        awr_response = awr.s3.to_parquet(
            df=df1,
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