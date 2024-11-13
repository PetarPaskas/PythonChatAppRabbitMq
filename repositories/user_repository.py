import csv
import uuid

users_file_name = 'users.csv'

def get_available_users():
    return [user for user in __get_users() if user[2] == True]

def user_exists(user_name, user_id=None): 
    users = __get_users()
    user = __find_user(users, user_name, user_id)
    return user == None

def __find_user(users, target_user_name, target_user_id=None):
    should_include_user_id = target_user_id != None
    for user in users:
        userid, username, available = user
        if should_include_user_id:
            if __match_by_user_id(target_user_id, userid) and __match_by_user_name(target_user_name, username):
                return user
        else:
            if __match_by_user_name(target_user_name, username) == True:
                return user
    return None

def __match_by_user_id(target_user_id, user_id):
    return target_user_id == user_id

def __match_by_user_name(target_user_name, user_name):
    return target_user_name == user_name


def add_user(user_name, user_id=None):   
    if not user_exists(user_name, user_id):
        return __add_user()

def __add_user(user_name, user_id=None):
    if user_id == None:
        user_id = uuid.uuid4()
    
    new_user = (user_id, user_name, True)

    users = __get_users()
    users.append(new_user)

    __write_to_users(users)
    return new_user


def set_user_availability(available, user_name, user_id=None): 
    users = __get_users()
    user = __find_user(users,user_name, user_id)
    if user == None: 
        return False
    return __update_user(user, (user_id, user_name, available))

def __get_users():
    with open(users_file_name, 'r') as users_file:
        users_csv = csv.reader(users_file)
        current_item = 0
        users = []
        for user in users_csv:
            if(current_item == 0):
                continue
            user_id, user_name, available = user
            users.append((user_id, user_name, available))
    return users

def __update_user(users, target_user, new_user):
    target_user_id = target_user[0]
    index_of_target_user = [index for index, user in enumerate(users) if user[0] == target_user_id][0]
    users[index_of_target_user] = new_user
    __write_to_users(users)

def __write_to_users(users):
    with open(users_file_name, 'w') as users_file:
        header = ['user_id', 'user_name', 'availability']
        users_csv = csv.writer(users_file)
        users_csv.writerow(header)

    for user in users:
        users_csv.writerow(user)