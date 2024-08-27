def main():
    user_login()
    sign_up()
    user_name()


def user_login():
    x = input('do you have a account YES / NO :').upper()
    if x == "YES":
        user_input()
    elif x == "NO":
        sign_up()
    else:
        print(f"invalid input")

def user_input(password,username):
    password = input("enter your password")
    username = input("enter your username: ")
    # 
    pass   

def sign_up():
    #sign up details need to be added to json file
    pass_list = []
    pass_word = input("create a password")
    pass_list.append(pass_word)
    print(f"your password is  : {pass_word}")


#creating username 
def user_name():
    x = []
    y = input("create a username: ")
    print(f'your user name is {y}@gmail.com') 
    x.append(y)   
     
# validate if the user input is valid and the pass word is strong







# ucceptence of details and ask to login






# Overwritte to a file to keep the data for futer login
main()