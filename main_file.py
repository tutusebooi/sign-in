import json
import re

def main():
    user_login()

def user_login():
    x = input('Do you have an account (YES / NO): ').upper()
    if x == "YES":
        user_input()
    elif x == "NO":
        sign_up()
    else:
        print("Invalid input. Please enter YES or NO.")
        user_login()

def user_input():
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    
    if validate_login(username, password):
        print("Login successful!")
    else:
        print("Invalid username or password.")
        user_login()

def validate_login(username, password):
    try:
        with open('user_data.json', 'r') as file:
            users = json.load(file)
            if username in users and users[username] == password:
                return True
    except FileNotFoundError:
        print("No users found. Please sign up.")
    return False

def sign_up():
    username = user_name()
    
    if username_exists(username):
        print("Username already exists. Please try again.")
        sign_up()
    else:
        password = create_password()
        save_user(username, password)
        print(f"Sign-up successful! You can now log in, {username}.")

def username_exists(username):
    try:
        with open('user_data.json', 'r') as file:
            users = json.load(file)
            return username in users
    except FileNotFoundError:
        return False

def create_password():
    while True:
        password = input("Create a password: ")
        if validate_password_strength(password):
            print(f"Your password is: {password}")
            return password
        else:
            print("Password not strong enough. Please try again.")

def validate_password_strength(password):
    # Password should be at least 8 characters long and include a number and special character
    if len(password) < 8:
        return False
    if not re.search(r"\d", password):  # check if there's a number
        return False
    if not re.search(r"[!@#$%^&*()_+]", password):  # check for special character
        return False
    return True

def user_name():
    return input("Create a username: ")

def save_user(username, password):
    try:
        with open('user_data.json', 'r') as file:
            users = json.load(file)
    except FileNotFoundError:
        users = {}
    
    users[username] = password
    with open('user_data.json', 'w') as file:
        json.dump(users, file)

main()
