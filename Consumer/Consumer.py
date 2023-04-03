import csv
import pika
import json

# Connect to RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Declare the queue
channel.queue_declare(queue='json_data')

# Open the CSV file
with open('output.csv', 'w', newline='') as file:
    writer = csv.writer(file)

    # Define the callback function
    def callback(ch, method, properties, body):

        # Load the JSON data from the message
        json_data = json.loads(body)

        # Write the row to the CSV file for each item in "preds"
        for pred in json_data['preds']:
            row = [json_data[key] for key in json_data.keys() if key != 'preds']
            row += [pred[key] for key in pred.keys()]
            writer.writerow(row)

    # Consume messages from the queue
    channel.basic_consume(queue='json_data', on_message_callback=callback, auto_ack=True)
    channel.start_consuming()