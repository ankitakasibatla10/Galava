import boto3
from openai import OpenAI

# Initialize the S3 client
s3_client = boto3.client('s3')


openai_client = OpenAI(api_key='YOUR_OPENAI_KEY')

def getMetadataSummary(data):
    # Assuming 'data' is a string that contains the metadata information
    # you want to summarize. Modify the message content as needed.
    response = openai_client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "Summarize this metadata. I want to vectorize this metadata, so please make the summary as detailed and accurate as possible: " + data},
        ]
    )
    # Assuming the response contains the summary in a format you expect
    # You might need to extract the exact field from the response depending on how the API returns it.
    summary = response.choices[0].message.content 
    print(summary)  

# List objects in the S3 bucket
response = s3_client.list_objects(Bucket='galavametadatabucket')

if 'Contents' in response:
    for obj in response['Contents']:
    
        object_response = s3_client.get_object(Bucket='galavametadatabucket', Key=obj['Key'])
        data = object_response['Body'].read().decode('utf-8')
        getMetadataSummary(data)
