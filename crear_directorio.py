import boto3

def lambda_handler(event, context):
    # Entrada (json)
    nombre_bucket = event['body']['bucket']
    directory = event['body']['directory']

    # Proceso
    s3 = boto3.client('s3')
    response = s3.put_object(
        Bucket=nombre_bucket,
        Body='',
        Key=directory + '/'
    )

    return {
        'statusCode': 200,
        'bucket': nombre_bucket,
        'response': response
    }
