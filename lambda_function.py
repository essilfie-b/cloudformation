import json

def lambda_handler(event, context):
    # Process the event
    print("Received event: " + json.dumps(event, indent=2))
    
    # Your custom logic here, for example, send an email or log something
    return {
        'statusCode': 200,
        'body': json.dumps('User notification processed successfully!')
    }
