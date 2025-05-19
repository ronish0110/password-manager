import random
import json
from utils import encode,decode

USERS_FILE = "password manager/users.json"
PASSWORDS_FILE = "password manager/passwords.json"

session_key = None
session_user = None
session_password = None

def start():
    while True:
        username = input('What is your Username: ').lower()
        is_existing_user = check_for_user(username)
        if is_existing_user:
            password = input('What is your Password: ')
            check_for_password(username, password)
        else:
            print(f"No user by the username {username}!")
            new_user = input("Do you want to create a new user(y/n): ")[0].lower()
            if new_user == "y":
                create_new_user()
            else:
                pass
    
def get_users():
    with open(USERS_FILE, "r") as users:
        return json.load(users)

def check_for_user(username):
    users = get_users()
    return (username in users.keys())

def create_new_user():
    while True:
        username = input("Enter new Username: ").lower()
        if check_for_user(username):
            print("Username already exists!")
            
        else:
            password = input("Enter the Password: ")
            add_user(username, password)
            return 0
    
def add_user(username, password):
    users = get_users()
    user_key = create_user_key(users)
    password = encode(password)
    users[username] = [password, user_key]
    update_users(users)
    
def update_users(new_users):
    with open(USERS_FILE, 'w') as users:
        json.dump(new_users, users)

def create_user_key(users_details):
    chars = ["A","B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k"]
    user_keys = []

    for key in users_details.keys():
        user_keys.append(users_details[key][1])

    while True:
        user_key = "".join(random.choices(chars, k = 7))
        user_key += str(random.randint(999, 999999))
        if user_key not in user_keys:
            return user_key
        
def check_for_password(username, password):
    users = get_users()
    if password == decode(users[username][0]):
        print("Login successfull!")
        global session_key, session_user, session_password
        session_key = users[username][1]
        session_user = username
        session_password = password
        show_home_screen()
    else:
        print("Incorrect username or password!!")

def show_home_screen():
    show_help()
    while True:
        choice = input("What do you want to do: ")[0].lower()
        perform(choice)

def show_help():
    print("""a to add a password
v to show all password
k to search password by name
d to delete a password
c to update a password
n to edit user details
h for help
q to quit application""")

def perform(choice):
    match choice:
        case "q":
            quit()
            return
        case "h":
            show_help()
            return
        case "v":
            show_users_password()
            return
        case "k":
            search_for_password()
        case "d":
            delete_password()
        case "c":
            update_password()
        case "n":
            edit_user()
        case "a":
            add_password()
        case _:
            print("invlaid option")

def add_password():
    passwords = get_users_password()
    name = input("Password Name: ")
    if name in passwords.keys():
        print(f"Password for {name} already exists!")
    else:
        password = input("Password: ")
        passwords[name] = encode(password)
        update_users_password(passwords)
        print(f"Password for {name} added successfully!")

        
def show_users_password():
    passwords = get_users_password()
    for key in passwords.keys():
        print(f"{key}:{decode(passwords[key])}")

def get_passwords():
    with open(PASSWORDS_FILE, "r") as password:
        all_passwords = json.load(password)
    return all_passwords

def get_users_password():
    all_passwords = get_passwords()
    return all_passwords[session_key]

def search_for_password():
    passwords = get_users_password()
    search = input("Search by Name: ")
    if search in passwords.keys():
        print(f"{search}:{decode(passwords[search])}")
    else:
        print(f"No passwrod of name {search} found")

def delete_password():
    passwords = get_users_password()
    show_users_password()
    name = input("Enter the name of password to delete: ")
    if name in passwords.keys():
        password = input("Enter your password: ")
        if password == session_password:
            del passwords[name]
            update_users_password(passwords)
        else:
            print("Incorrect password")
    else:
        print(f"No password by the name {name}")

def update_users_password(password):
    all_passwords = get_passwords()
    all_passwords[session_key] = password
    with open(PASSWORDS_FILE, "w") as f:
        json.dump(all_passwords, f)

def update_password():
    show_users_password()
    passwords = get_users_password()
    name = input('Update password by name: ')
    if name in passwords.keys():
        password = input('Enter user password: ')
        if password == session_password:
            new_password = input("Enter new password: ")
            new_password = encode(new_password)
            passwords[name] = new_password
            update_users_password(passwords)
        else:
            print("Incorrect password!")
    else:
        print(f"No password by the name {name}")

def edit_user():
    password = input("Entre your password to edit: ")
    global session_password, session_user
    if password == session_password:

        print(f"Username(1) : {session_user}")
        print(f"Password(2) : {session_password}")
        choice = input("What do you want to change: ")[0]

        if choice == "1":
            new_username = input('New Username: ').lower()
            users = get_users()
            users[new_username] = users[session_user]
            del users[session_user]
            session_user = new_username
            update_users(users)

        elif choice == "2":
            new_password = input("New password: ")
            session_password = new_password
            users = get_users()
            users[session_user][0] = encode(new_password)
            with open(USERS_FILE, 'w') as f:
                json.dump(users, f)
            print('Password changed successfully!')
        else:
            print("Invalid option!")

if __name__ == "__main__":
    start()
