import boto3

def lambda_handler(event, context):
    s3 = boto3.client('s3')
    bucket_name = event['bucket_name']
    
    response = s3.create_bucket(
        Bucket=bucket_name,
        ACL='public-read'
    )
    
    return {
        'statusCode': 200,
        'body': f'Bucket {bucket_name} creado con exito :D',
        'Location': response['Location']
    }
