import json
import boto3
from botocore.exceptions import ClientError

def lambda_handler(event, context):
    # Initialize the S3 client
    s3_client = boto3.client('s3')

    # Retrieve bucket name and region from the event
    bucket_name = event.get('bucket_name', 'default-bucket-name')
    region = event.get('region', 'us-east-1')  # Default to 'us-east-1' if not provided

    try:
        # Create the S3 bucket
        response = s3_client.create_bucket(
            Bucket=bucket_name,
            CreateBucketConfiguration={
                'LocationConstraint': region
            }
        )
        return {
            'statusCode': 200,
            'body': json.dumps(f'Successfully created bucket: {bucket_name}')
        }
        
    except ClientError as e:
        return {
            'statusCode': 501,
            'body': json.dumps(f'Error: {str(e)}')
        }
