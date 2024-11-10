# from chat.chat_consumer import ChatConsumer
# from comms.publisher.publisher import Publisher

# queue_name='letterbox'

# first_publisher = Publisher(queue_name)

# first_publisher.publish('','This is my first message')

# first_consumer = ChatConsumer(queue_name)

import csv 

users_file_name = 'users.csv'

# with open(users_file_name, 'r') as users_file:
#     users_csv = csv.reader(users_file)
#     for x in users_csv:
#         first, second, third = x
#         print(first, second, third)

users = [
    (1, 'Alice', 'Available'),
    (4, 'Charlie', 'Available'),
    (2, 'Bob', 'Busy'),
    (3, 'Charlie', 'Available')
]

target_user_id = 4
index_of_target_user = [index for index, user in enumerate(users) if user[0] == target_user_id]
print(f'target: {index_of_target_user}')
with open(users_file_name, 'w') as users_file:
    header = ['user_id', 'user_name', 'availability']
    users_csv = csv.writer(users_file)
    users_csv.writerow(header)
        
    for user in users:
        users_csv.writerow(user)