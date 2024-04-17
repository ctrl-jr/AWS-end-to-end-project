
#Generated on AWS - Visual ETL Job - drops a few columns from the parquet file
import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job

args = getResolvedOptions(sys.argv, ['JOB_NAME'])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# Script generated for node Amazon S3
AmazonS3_node1713059984014 = glueContext.create_dynamic_frame.from_options(format_options={}, connection_type="s3", format="parquet", connection_options={"paths": ["s3://jr-s3-clean-data"], "recurse": True}, transformation_ctx="AmazonS3_node1713059984014")

# Script generated for node Select Fields
SelectFields_node1713060165795 = SelectFields.apply(frame=AmazonS3_node1713059984014, paths=["index", "name", "releasedate", "topcriticscore"], transformation_ctx="SelectFields_node1713060165795")

job.commit()

