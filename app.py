from prompting.console_interactions import read_client_name, choose_who_to_chat_with
from repositories.user_repository import add_user, set_user_availability

def initiate_current_user():
    client_name = read_client_name()
    return add_user(client_name)

def initiate_as_publisher():
    current_user_id, current_user_name, current_user_availability  = initiate_current_user()
    target_user_id, target_user_name, target_user_availability  = choose_who_to_chat_with()
    #initiate chat app as publisher 
    chat = None
    set_user_availability(False, current_user_name, current_user_id)
    return (chat)

def initiate_as_consumer():
    current_user_id, current_user_name, current_user_availability = initiate_current_user()
    #initiate chat app as consumer 
    chat = None
    set_user_availability(False, current_user_name, current_user_id)
    return (chat)


option = int(input("Do you want to find people or people to find you?\n1. I want to find people\2. I want peple to find me"))

should_initiate_as_publisher = option == 1
should_initiate_as_consumer = option == 2

if should_initiate_as_publisher:
    initiate_as_publisher()
else:
    if should_initiate_as_consumer:
        initiate_as_consumer()

