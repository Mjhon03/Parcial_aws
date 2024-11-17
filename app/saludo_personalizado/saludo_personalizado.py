import json

def saludo_personalizado(event, context):
    """
    Lambda function to return a personalized greeting.
    Supports input from query string or body.
    """
    params = event.get("queryStringParameters", {})
    nombre = params.get("nombre") if params else None

    if not nombre:
        try:
            body = json.loads(event.get("body", "{}"))
            nombre = body.get("nombre", "").strip()
        except Exception:
            nombre = None

    if not nombre:
        return {
            "statusCode": 400,
            "body": json.dumps({"error": "El parámetro 'nombre' es obligatorio y no puede estar vacío."}),
            "headers": {"Content-Type": "application/json"}
        }

    return {
        "statusCode": 200,
        "body": json.dumps({"message": f"Hola, {nombre}!"}),
        "headers": {"Content-Type": "application/json"}
    }

