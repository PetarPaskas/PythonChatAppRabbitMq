import pika 

connection_parameters = pika.ConnectionParameters('localhost')
mqConnection = pika.BlockingConnection(connection_parameters)

