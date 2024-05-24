from tkinter import *
from tkinter import messagebox
 
 
def login():
    username = entry_username.get()
    password = entry_password.get()
 
 
    if username == "admin" and password == "admin":
        messagebox.showinfo("Login", "Login successful")
    else:
        messagebox.showerror("Login Error", "Incorrect username or password")
 
 
# Create the main window
root = Tk()
root.title("Login - The Pycodes")
root.geometry("300x150")
 
 
# Username label and entry
label_username = Label(root, text="Username:")
label_username.pack()
entry_username = Entry(root)
entry_username.pack()
 
 
# Password label and entry
label_password = Label(root, text="Password:")
label_password.pack()
entry_password = Entry(root, show="*") # Show asterisks for password input
entry_password.pack()
 
 
# Login button
login_button = Button(root, text="Login", command=login)
login_button.pack()
 
 
# Start the main event loop
root.mainloop()
