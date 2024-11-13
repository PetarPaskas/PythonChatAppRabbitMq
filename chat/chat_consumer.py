from comms.consumer.consumer import Consumer

class ChatConsumer(Consumer):
    def __init__(self, consumer_name, handle_chat_init):
        super().__init__(consumer_name)
        self.handle_chat_init = handle_chat_init

    def consume(self, message_headers, message_body):
        print(f'[INFO]: {message_body}')

    def __on_chat_init(self, message_body):
        if message_body == 'chat_init':
            requestor_queue = ''
            self.handle_chat_init(requestor_queue)

