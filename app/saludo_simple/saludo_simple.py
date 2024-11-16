import json

def saludo_simple():
  return {
    "statusCode":200,
    "body": json.dumps({"message":"Hola, bienvenido al sistema"})
  }
