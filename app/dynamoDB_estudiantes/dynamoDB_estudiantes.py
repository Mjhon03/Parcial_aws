import json
import boto3
from botocore.exceptions import ClientError

# Crear un cliente de DynamoDB
dynamodb = boto3.client("dynamodb")

def dynamoDB_estudiantes(event, context):
    """
    Lambda function to fetch student data from a DynamoDB table.

    Args:
        event (dict): The event payload containing request data.
        context (object): AWS Lambda context object.

    Returns:
        dict: HTTP response with student data or error message.
    """
    params = event.get("queryStringParameters", {})
    student_id = params.get("id") if params else None

    if not student_id:
        return {
            "statusCode": 400,
            "body": json.dumps({"error": "El parámetro 'id' es obligatorio."}),
            "headers": {"Content-Type": "application/json"}
        }

    try:
  
        response = dynamodb.get_item(
            TableName="Estudiantes",
            Key={"id": {"S": student_id}}
        )

  
        if "Item" not in response:
            return {
                "statusCode": 404,
                "body": json.dumps({"error": f"No se encontró el estudiante con id '{student_id}'."}),
                "headers": {"Content-Type": "application/json"}
            }

  
        estudiante = {
            "id": response["Item"]["id"]["S"],
            "nombre": response["Item"]["nombre"]["S"],
            "carrera": response["Item"]["carrera"]["S"]
        }

        return {
            "statusCode": 200,
            "body": json.dumps(estudiante),
            "headers": {"Content-Type": "application/json"}
        }

    except ClientError as e:
  
        return {
            "statusCode": 500,
            "body": json.dumps({"error": f"Error al conectar con DynamoDB: {str(e)}"}),
            "headers": {"Content-Type": "application/json"}
        }
