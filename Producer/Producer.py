import pika
import json

# Open the JSON file
with open('Producer/POST.json', 'r') as file:
    
    json_data = json.load(file)

# Check for low probability and append tag
for js in json_data['data']['preds']:

    if js['prob'] < 0.25:

        js['tags'].append('low_prob')

# Connect to RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Declare the queue
channel.queue_declare(queue='json_data')

# Convert the JSON data to a string
message = json.dumps(json_data)

# Publish the message to the queue
channel.basic_publish(exchange='', routing_key='json_data', body=message)
print(f"sent message: {message}")

# Close the connection
connection.close()