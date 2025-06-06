import sys
import pipeline
def handler(event, context):
  if '.' not in sys.path:
    sys.path.insert(0, '.')

  try:
    pipeline.main()
    return {
      "statusCode": 200,
      "body": "Success!"
    }
  except Exception as e:
    print(e)
    return {
      "statusCode": 500,
      "body": str(e)
    }