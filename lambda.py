#Lambda1: Serialize Image data
import json
import boto3
import base64

s3 = boto3.client('s3')

def lambda_handler(event, context):
    
    print("Received event:", json.dumps(event, indent=2))
    
    key = event.get('s3_key')  
    bucket = event.get('s3_bucket')  
    
    # Check if key and bucket are present
    if not key or not bucket:
        print(f"Key: {key}, Bucket: {bucket}")  
        raise ValueError("Missing 's3_key' or 's3_bucket' in event")

    try:
        s3.download_file(bucket, key, '/tmp/image.png')  
    except Exception as e:
        raise RuntimeError(f"Failed to download file from S3: {str(e)}")

    with open("/tmp/image.png", "rb") as f:
        image_data = base64.b64encode(f.read()).decode('utf-8')  

    return {
        'statusCode': 200,
        'body': {
            "s3_bucket": bucket,
            "s3_key": key,
            "image_data": image_data,
            "inferences": []
        }
    }

#Lambda2: Classify Images
import json
import boto3
import base64

sagemaker_runtime = boto3.client('runtime.sagemaker')

ENDPOINT = "image-classification-2024-09-23-04-57-10-567"  

def lambda_handler(event, context):

    if "body" not in event or "image_data" not in event["body"]:
        return {
            'statusCode': 400,
            'body': json.dumps({"error": "Invalid input, 'image_data' not found"})
        }
    
    try:
        image = base64.b64decode(event["body"]["image_data"])
    except Exception as e:
        return {
            'statusCode': 400,
            'body': json.dumps({"error": f"Failed to decode image data: {str(e)}"})
        }

    try:
        response = sagemaker_runtime.invoke_endpoint(
            EndpointName=ENDPOINT,
            ContentType="image/png",  
            Body=image
        )

        inferences = json.loads(response['Body'].read().decode())
        
        event["body"]["inferences"] = inferences
        return {
            'statusCode': 200,
            'body': event["body"]
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({"error": f"Prediction failed: {str(e)}"})
        }
#Lambda3: Image Inference
import json

THRESHOLD = 0.73

def lambda_handler(event, context):

    body = json.loads(event["body"])
    
    inferences = body.get("inferences", [])
    
    meets_threshold = any(prob >= THRESHOLD for prob in inferences)
    
    if meets_threshold:
        return {
            'statusCode': 200,
            'body': json.dumps(body)
        }
    else:
        return {
            'statusCode': 400,
            'body': json.dumps({"message": "THRESHOLD_CONFIDENCE_NOT_MET"})
        }

