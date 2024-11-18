import json

def calculadora_basica(event, context):
    """
    Lambda function to perform basic arithmetic operations (+, -, *, /).
    Validates that 'a' and 'b' are numeric and 'operador' is valid.

    Args:
        event (dict): The event payload containing request data.
        context (object): AWS Lambda context object.

    Returns:
        dict: HTTP response with the operation result or error message.
    """
    # Obtener los parámetros de la URL
    params = event.get("queryStringParameters", {})

    if not params or not all(key in params for key in ["a", "b", "operador"]):
        return {
            "statusCode": 400,
            "body": json.dumps({"error": "Los parámetros 'a', 'b' y 'operador' son obligatorios."}),
            "headers": {"Content-Type": "application/json"}
        }

    a = params.get("a")
    b = params.get("b")
    operador = params.get("operador")

    try:
        a = float(a)
        b = float(b)
    except ValueError:
        return {
            "statusCode": 400,
            "body": json.dumps({"error": "Los parámetros 'a' y 'b' deben ser valores numéricos."}),
            "headers": {"Content-Type": "application/json"}
        }

    if operador not in ["+", "-", "*", "/"]:
        return {
            "statusCode": 400,
            "body": json.dumps({"error": "El operador debe ser uno de los siguientes: +, -, *, /."}),
            "headers": {"Content-Type": "application/json"}
        }

    try:
        if operador == "+":
            resultado = a + b
        elif operador == "-":
            resultado = a - b
        elif operador == "*":
            resultado = a * b
        elif operador == "/":
            if b == 0:
                raise ZeroDivisionError("No se puede dividir por cero.")
            resultado = a / b
    except ZeroDivisionError as e:
        return {
            "statusCode": 400,
            "body": json.dumps({"error": str(e)}),
            "headers": {"Content-Type": "application/json"}
        }

    return {
        "statusCode": 200,
        "body": json.dumps({"resultado": resultado}),
        "headers": {"Content-Type": "application/json"}
    }
