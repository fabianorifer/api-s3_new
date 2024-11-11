import boto3

def lambda_handler(event, context):
    s3 = boto3.client('s3')
    
    # Verificar si 'bucket_name' está en event
    if 'bucket_name' not in event:
        return {
            'statusCode': 400,
            'body': 'Error: El campo bucket_name es obligatorio.'
        }

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
