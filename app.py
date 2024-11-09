from chat.chat_consumer import ChatConsumer
from comms.publisher.publisher import Publisher

queue_name='letterbox'

first_publisher = Publisher(queue_name)

first_publisher.publish('','This is my first message')

first_consumer = ChatConsumer(queue_name)
