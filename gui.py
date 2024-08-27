import tkinter as tk

def user_interfase():
    root= tk.Tk()

    root.geometry("500x500")
    root.title("Welcome page")

    label = tk.Label(root, text="Sign up/Sign in",font=("Bold", 15))
    label.pack()
    text_box = tk.Text(root, height=2,font=("bold",16))
    text_box.pack(padx=10)

    button = tk.Button(root,text="ENTER", font=("Bold", 18))
    button.pack()
    #tk.CENTER()


    root.mainloop()
user_interfase()