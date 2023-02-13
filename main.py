import time
import pika
import consumer
import producer

credentials = pika.PlainCredentials('user', 'password')
parameters = pika.ConnectionParameters(
    '127.0.0.1', 5762, '/', credentials)

queue_name = "testqueue_amqp_0-9"

for i in range(0,10):
    message = {'name': 'John Doe', 'age':33, 'ID': i}
    producer.write(parameters, queue_name, message)

time.sleep(5)
print("--- consume un-acked messages from RabbitMQ queue ---")

while consumer.read(parameters, queue_name):
    consumer.read(parameters, queue_name)