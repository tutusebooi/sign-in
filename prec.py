def main():
    user_login()
    sign_up()
    user_name()
# user log in or sing up

def user_login():
    x = input('do you have a account: YES / NO ').upper()
    if x == "YES":
        #return f"PLEASE LOGIN"
        print(input("enter your password"))
    elif x == "NO":
        sign_up()
    else:
        print(f"invalid input")    

def sign_up():
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
main()






# ucceptence of details and ask to login






# Overwritte to a file to keep the data for futer login