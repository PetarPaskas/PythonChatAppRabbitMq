from comms.consumer.consumer import Consumer

class ChatConsumer(Consumer):
    def __init__(self, consumer_name):
        super().__init__(consumer_name)

    def consume(self, message_headers, message_body):
        print(f'{self.consumer_name} listening: ')
        print(f'body: {message_body}')
