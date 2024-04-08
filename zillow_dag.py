from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.bash_operator import BashOperator
from airflow.providers.amazon.aws.sensors.s3 import S3KeySensor
from airflow.providers.amazon.aws.transfers.s3_to_redshift import S3ToRedshiftOperator

from etl import run_zillow_etl

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2024, 1, 1),
    'email': ['airflow@example.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 2,
    'retry_delay': timedelta(seconds=15)
}

dag = DAG(
    'zillow_dag',
    default_args=default_args,
    description='Zillow games API',
    schedule_interval=timedelta(days=1),
)

run_etl = PythonOperator(
    task_id='tsk_extract_data',
    python_callable=run_zillow_etl,
    dag=dag, 
)

upload_to_s3 = BashOperator(
    task_id = 'tsk_upload_to_s3)',
    bash_command = 'aws s3 mv {{ ti.xcom_pull("tsk_extract_zillow_data_var")[0]}} s3://jr-bucket-0002/',
)
run_etl