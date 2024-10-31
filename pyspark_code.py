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

predicate_pushdown = "region in ('ca','gb','us')"

# Reading data from S3 with pushDownPredicate
AmazonS3_node = glueContext.create_dynamic_frame.from_options(
    format_options={"quoteChar": "\"", "withHeader": True, "separator": ",", "optimizePerformance": False}, 
    connection_type="s3", 
    format="csv", 
    connection_options={"paths": ["s3://de-on-youtube-raw-ap-south-dev-1/youtube/raw-statistics/"], "recurse": True, "pushDownPredicate": predicate_pushdown}, 
    transformation_ctx="AmazonS3_node"
)

# Applying schema transformations (Change Schema)
ChangeSchema_node = ApplyMapping.apply(
    frame=AmazonS3_node, 
    mappings=[
        ("video_id", "string", "video_id", "string"),
        ("trending_date", "string", "trending_date", "string"),
        ("title", "string", "title", "string"),
        ("channel_title", "string", "channel_title", "string"),
        ("category_id", "string", "category_id", "string"),
        ("publish_time", "string", "publish_time", "string"),
        ("tags", "string", "tags", "string"),
        ("views", "string", "views", "string"),
        ("likes", "string", "likes", "string"),
        ("dislikes", "string", "dislikes", "string"),
        ("comment_count", "string", "comment_count", "string"),
        ("thumbnail_link", "string", "thumbnail_link", "string"),
        ("comments_disabled", "string", "comments_disabled", "string"),
        ("ratings_disabled", "string", "ratings_disabled", "string"),
        ("video_error_or_removed", "string", "video_error_or_removed", "string"),
        ("description", "string", "description", "string")
    ], 
    transformation_ctx="ChangeSchema_node"
)

# Writing the transformed data back to S3 in Parquet format
glueContext.write_dynamic_frame.from_options(
    frame=ChangeSchema_node, 
    connection_type="s3", 
    format="glueparquet", 
    connection_options={"path": "s3://de-on-youtube-cleansed-ap-south-dev-1/youtube/raw-statistics/", "partitionKeys": []}, 
    format_options={"compression": "snappy"}, 
    transformation_ctx="AmazonS3_node_write"
)

job.commit()
