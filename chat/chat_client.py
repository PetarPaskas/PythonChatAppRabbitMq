from chat.chat_consumer import ChatConsumer
from chat.chat_publisher import ChatPublisher

class ChatClient:
    @classmethod
    def initiate_as_consumer(consumer_name):
        chat = ChatClient(consumer_name)
        chat.initiate_consumer()
        producer_name = chat.consumer_for_init_command()
        chat.initiate_producer(producer_name)
        return chat

    @classmethod
    def initiate_as_publisher(publisher_name, target_to_publish_to):
        #initiate full chat client
        #send chat_init command to consumer
        chat = ChatClient(publisher_name,target_to_publish_to)
        chat.initiate_consumer()
        chat.initiate_producer()
        chat.publish_init_command()
        #chat background consuming
        return chat

    def __init__(self, consumer_name, target_name=None):
        self.consumer_name = consumer_name
        self.target_name = target_name

    def initiate_consumer(self):
        self.chat_consumer = ChatConsumer(consumer_name=self.consumer_name)
        #initiate consuming and messaging funcitonalities 

    def initiate_producer(self, target_name=None):
        target_to_produce_to = self.target_name
        if(target_name != None and target_to_produce_to == None):
            target_to_produce_to = target_name

        self.chat_publisher = ChatPublisher(target_to_produce_to)
    
    def publish_init_command(self):
        self.chat_publisher.publish('chat_init')

    def consumer_for_init_command(self):
        pass



    