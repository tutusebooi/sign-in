import tkinter as tk
from main_file import user_input  # assuming you're importing user_input for later use

def user_interface():
    root = tk.Tk()

    # Set window size and title
    root.geometry("500x500")
    root.title("Welcome Page")

    # Label for the window
    label = tk.Label(root, text="Sign up / Sign in", font=("Bold", 15))
    label.pack(pady=20)

    # Text box for the username
    username_label = tk.Label(root, text="Username:", font=("bold", 12))
    username_label.pack(pady=10)
    username_entry = tk.Entry(root, font=("bold", 14))
    username_entry.pack(padx=10, pady=10)

    # Text box for the password
    password_label = tk.Label(root, text="Password:", font=("bold", 12))
    password_label.pack(pady=10)
    password_entry = tk.Entry(root, font=("bold", 14), show="*")  # Masking input for password
    password_entry.pack(padx=10, pady=10)

    # Button to handle the submission
    def on_enter():
        username = username_entry.get()
        password = password_entry.get()
        # Here you can call your user_input() function or other login/signup logic
        print(f"Username: {username}, Password: {password}")

    button = tk.Button(root, text="ENTER", font=("Bold", 18), command=on_enter)
    button.pack(pady=20)

    root.mainloop()

user_interface()
