
import pika
from abc import ABC, abstractmethod  
from comms.connection import mqConnection

class Publisher:

    def __init__(self, publish_destination):
        self.publish_destination = publish_destination
        self.__setup_channel_and_queue(publish_destination)

    def publish(self, message_headers, message_body):
        self.channel.basic_publish(exchange='',routing_key=self.publish_destination,body=message_body, properties=message_headers) 

    def __setup_channel_and_queue(self, queue_name):
        self.channel = mqConnection.channel()
        self.channel.queue_declare(queue_name)
    