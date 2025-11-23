import boto3
import os

def get_sns_client():
    # Tenta obter credenciais do ambiente ou usa profile default
    return boto3.client('sns', region_name=os.getenv('AWS_REGION', 'us-east-1'))

def send_alert_email(subject, message):
    """
    Envia um alerta via AWS SNS (que pode entregar por email/SMS).
    Requer que o tópico ARN esteja configurado ou cria um para teste.
    """
    try:
        sns = get_sns_client()
        
        # Para simplificar, vamos publicar em um tópico fixo ou criar um
        # Em produção, o ARN viria de config
        topic_arn = os.getenv('AWS_SNS_TOPIC_ARN')
        
        if not topic_arn:
            # Fallback: Log apenas se não tiver ARN configurado
            print(f"[MOCK AWS] Enviando alerta: {subject} - {message}")
            return True
            
        response = sns.publish(
            TopicArn=topic_arn,
            Message=message,
            Subject=subject
        )
        return response
    except Exception as e:
        print(f"Erro ao conectar com AWS: {e}")
        # Em ambiente de dev sem credenciais, não queremos quebrar a app
        raise e

def send_alert_sms(phone_number, message):
    try:
        sns = get_sns_client()
        response = sns.publish(
            PhoneNumber=phone_number,
            Message=message
        )
        return response
    except Exception as e:
        print(f"Erro ao enviar SMS: {e}")
        raise e
