import json

def procesamiento_texto(event, context):
    """
    Lambda function to process a text input and return the number of words,
    number of characters, and the text in uppercase.

    Args:
        event (dict): The event payload containing request data.
        context (object): AWS Lambda context object.

    Returns:
        dict: HTTP response with word count, character count, and uppercase text.
    """
    try:
        # Obtener el texto directamente desde el evento
        texto = event.get("texto")
        if not texto:
            return {
                "statusCode": 400,
                "body": json.dumps({"error": "El parámetro 'texto' es obligatorio."}),
                "headers": {"Content-Type": "application/json"}
            }

        # Procesar el texto
        palabras = len(texto.split())
        caracteres = len(texto)
        texto_mayusculas = texto.upper()

        # Respuesta
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

    except Exception as e:
        # Manejo de errores generales
        return {
            "statusCode": 500,
            "body": json.dumps({"error": f"Error interno del servidor: {str(e)}"}),
            "headers": {"Content-Type": "application/json"}
        }
