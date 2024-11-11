import boto3
import base64

def lambda_handler(event, context):
    s3 = boto3.client('s3')
    bucket_name = event['bucket_name']
    directory_name = event['directory_name']
    file_name = event['file_name']
    file_content = base64.b64decode(event['file_content'])
    
    s3.put_object(Bucket=bucket_name, Key=f'{directory_name}/{file_name}', Body=file_content)
    
    return {
        'statusCode': 200,
        'body': f'Archivo {file_name} subido a {bucket_name}/{directory_name}'
    }
