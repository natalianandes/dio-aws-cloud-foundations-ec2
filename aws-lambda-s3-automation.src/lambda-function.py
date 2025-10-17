import json
import boto3

def lambda_handler(event, context):
    s3 = boto3.client('s3')
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = event['Records'][0]['s3']['object']['key']
    
    try:
        response = s3.get_object(Bucket=bucket, Key=key)
        content = response['Body'].read().decode('utf-8')
        data = json.loads(content)
        
        print(f"Arquivo processado com sucesso: {key}")
        return {'statusCode': 200, 'body': json.dumps('Processamento concluído!')}
        
    except Exception as e:
        print(f"Erro ao processar {key}: {e}")
        return {'statusCode': 500, 'body': json.dumps('Erro no processamento')}
