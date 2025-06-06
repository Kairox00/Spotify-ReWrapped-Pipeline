import sys
def handler(event, context):
  if '.' not in sys.path:
    sys.path.insert(0, '.')

  import pipeline

  return {
    "statusCode": 200,
    "body": "Hello from Lambda!"
  }

handler(None, None)