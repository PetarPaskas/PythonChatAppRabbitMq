from repositories.user_repository import user_exists, get_available_users
import os 
def clear_window():
    os.system('cls')

def read_client_name():
    client_name = None 
    while(client_name == None):
        client_name = __get_client_name()
        if(client_name == None):
            clear_window()
            print('Client name was invalid, try again.')

def choose_who_to_chat_with():
    print("Choose who you want to chat with by inputing their index")
    users = get_available_users()
    for (index, user) in enumerate(users):
        user_id, user_name, availability = user
        print(f'{index}: {user_name}')

    user_chosen = input('Index: ')
    index = int(user_chosen)
    
    return users[index]

def __get_client_name():
    client_name = input('Input your name\nRules:\n- can\'t be empty\n- no whitespace\n- no duplicates')
    return client_name if __check_client_name_input_acceptable(client_name) else None

def __check_client_name_input_acceptable(client_name):
    return client_name and not client_name.contains(' ') and not user_exists(client_name)
