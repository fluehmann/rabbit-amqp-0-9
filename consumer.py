import pika


def read(parameters: pika.ConnectionParameters, queue_name: str):
    connection = pika.BlockingConnection(parameters)
    channel = connection.channel()

    print("Consumer connected: " + str(parameters))

    method_frame, header_frame, body = channel.basic_get(queue=queue_name)

    if method_frame:
        print("Message received: " + str(body))
        channel.basic_ack(method_frame.delivery_tag, False)
    else:
        print("--- no new messages detected ---")

    channel.close()
    connection.close()