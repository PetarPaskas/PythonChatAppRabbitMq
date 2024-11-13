from comms.publisher.publisher import Publisher

class ChatPublisher:
    def __init__(self, target_user):
        self.target_user = target_user
        self.publisher = Publisher(target_user)

    def publish(self, message):
        headers = self.__set_headers()
        self.publisher.publish(headers, message)

    def __set_headers(self):
        return None