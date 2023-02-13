import pika
import json


def write(parameters: pika.ConnectionParameters, queue_name: str, message):
    connection = pika.BlockingConnection(parameters)
    channel = connection.channel()

    print("Producer connected: " + str(parameters))

    channel.queue_declare(queue=queue_name)
    channel.basic_publish(exchange='', routing_key=queue_name,
                          body=json.dumps(message))

    print("Message sent: " + str(message))

    channel.close()
    connection.close()
