import boto3
import base64

def lambda_handler(event, context):
    # Entrada (json)
    nombre_bucket = event['body']['bucket']
    base_64_file = event['body']['base_64_file']
    file_name = event['body']['file_name']
    directory = event['body']['directory']

    # Proceso
    s3 = boto3.client('s3')
    response = s3.put_object(
        Bucket=nombre_bucket,
        Body=base64.b64decode(base_64_file),
        Key=directory + '/' + file_name
    )

    return {
        'statusCode': 200,
        'bucket': nombre_bucket,
        'response': response
    }
