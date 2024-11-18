import json

def saludo_simple(event,context):
  return {
    "statusCode":200,
    "body": json.dumps({"message":"Hola, bienvenido al sistema"})
  }
