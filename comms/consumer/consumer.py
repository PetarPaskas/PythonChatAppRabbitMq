
import pika
from abc import ABC, abstractmethod  

from comms.connection import mqConnection


class Consumer(ABC):
    
    def __init__(self, consumer_name):
        self.consumer_name = consumer_name
        self.__setup_channel_and_queue(consumer_name)
        self.start_consuming()

    @abstractmethod
    def consume(self, message_headers, message_body):
        pass 

    def start_consuming(self):
        self.channel.basic_consume(self.consumer_name, auto_ack=True, on_message_callback=self.__listen)
        self.channel.start_consuming()

    def stop_consuming(self):
        self.channel.stop_consuming()

    def __setup_channel_and_queue(self, queue_name):
        self.channel = mqConnection.channel()
        self.channel.queue_declare(queue_name)

    def __listen(self, ch, method, properties, body):
        self.consume(properties, body)

    