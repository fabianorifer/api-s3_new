import json
import boto3
from botocore.exceptions import ClientError

def lambda_handler(event, context):
    s3_client = boto3.client('s3')
    bucket_name = event.get('bucket_name', 'default-bucket-name')
    region = event.get('region', 'us-east-1')

    try:
        # Crea el bucket sin LocationConstraint para us-east-1
        if region == 'us-east-1':
            response = s3_client.create_bucket(Bucket=bucket_name)
        else:
            response = s3_client.create_bucket(
                Bucket=bucket_name,
                CreateBucketConfiguration={'LocationConstraint': region}
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
