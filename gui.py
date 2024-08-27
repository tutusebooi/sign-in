import tkinter as tk
from main_file import *

def user_interfase():
    root= tk.Tk()

    root.geometry("500x500")
    root.title("Welcome page")
    root.baseName("xolela")
    label = tk.Label(root, text="Sign up/Sign in",font=("Bold", 15))
    username = tk(user_input())
    username_botton = tk.Button(root,username)
    label.pack()
    text_box = tk.Text(root, height=2,font=("bold",16))
    text_box.pack(padx=10)

    button = tk.Button(root,text="ENTER", font=("Bold", 18))
    button.pack()
    #tk.CENTER()


    root.mainloop()
user_interfase()