import boto3

def lambda_handler(event, context):
    s3 = boto3.client('s3')
    bucket_name = event['bucket_name']
    directory_name = event['directory_name']
    
    s3.put_object(Bucket=bucket_name, Key=(directory_name + '/'))
    
    return {
        'statusCode': 200,
        'body': f'Directorio {directory_name} creado en {bucket_name}'
    }
