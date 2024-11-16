import json

def saludo_personalizado(event, context):
    """
    Lambda function to return a personalized greeting.
    Validates if the 'nombre' parameter is provided in the query string.

    Args:
        event (dict): The event payload containing request data.
        context (object): AWS Lambda context object.

    Returns:
        dict: HTTP response with greeting or error message.
    """
    params = event.get("queryStringParameters", {})

    if not params or "nombre" not in params:
      if params["nombre"] == "":
          return {
              "statusCode": 400,
              "body": json.dumps({"error": "El parámetro 'nombre' es obligatorio."}),
              "headers": {"Content-Type": "application/json"}
          }

    nombre = params["nombre"]

    return {
        "statusCode": 200,
        "body": json.dumps({"message": f"Hola, {nombre}!"}),
        "headers": {"Content-Type": "application/json"}
    }
