import json

def procesamiento_texto(event, context):
    """
    Lambda function to process a text input and return the number of words,
    number of characters, and the text in uppercase.
    Accepts the input from either 'event["texto"]' or 'event["body"]'.

    Args:
        event (dict): The event payload containing request data.
        context (object): AWS Lambda context object.

    Returns:
        dict: HTTP response with word count, character count, and uppercase text.
    """
    try:
        texto = event.get("texto")

        if not texto:
            body = event.get("body", "{}")  
            body_data = json.loads(body) if isinstance(body, str) else body
            texto = body_data.get("texto")

        if not texto:
            return {
                "statusCode": 400,
                "body": json.dumps({"error": "El parámetro 'texto' es obligatorio en el cuerpo o en el evento."}),
                "headers": {"Content-Type": "application/json"}
            }

        palabras = len(texto.split())
        caracteres = len(texto)
        texto_mayusculas = texto.upper()

        respuesta = {
            "palabras": palabras,
            "caracteres": caracteres,
            "texto_mayusculas": texto_mayusculas
        }

        return {
            "statusCode": 200,
            "body": json.dumps(respuesta),
            "headers": {"Content-Type": "application/json"}
        }

    except json.JSONDecodeError:
        return {
            "statusCode": 400,
            "body": json.dumps({"error": "El cuerpo de la solicitud debe estar en formato JSON válido."}),
            "headers": {"Content-Type": "application/json"}
        }
    except Exception as e:
        # Manejo de errores generales
        return {
            "statusCode": 500,
            "body": json.dumps({"error": f"Error interno del servidor: {str(e)}"}),
            "headers": {"Content-Type": "application/json"}
        }
