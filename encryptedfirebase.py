from tkinter import *
from firebase import firebase
from simplecrypt import encrypt, decrypt

root = Tk()
root.title("Firebase Encryption")
root.geometry("800x600")
root.config(bg="#F85E00")

firebase = firebase.FirebaseApplication("https://encryptedhw-f9957-default-rtdb.firebaseio.com/", None)

login_username_entry = ""
login_password_entry = ""

def register():
    username = username_entry.get()
    password = password_entry.get()
    result = hashlib.md5(password.encode())
    formatted = hexdigest(result)
    print(formatted)
    firebase.put("/", password, formatted)
    
def login_window():
    global login_username_entry, login_password_entry
    root.close()
    login = Tk()
    login.config(bg="#F85E00")
    login.title("Login")
    login.geometry("800x600")
    header = Label(login, fg="#1E212B", text="Login Page", bg="#F85E00" , font=("Comic Sans MS", "25", "bold"))
    header.place(relx=0.5, rely=0.05, anchor=CENTER)
    
    login_username_label = Label(login, text="username", fg="#", bg="#F85E00", font=("Comic Sans MS", "17", "bold"))
    login_username_label.place(relx=0.3, rely=0.2, anchor=CENTER)
    login_password_label = Label(login, text="password" , fg="#", bg="#F85E00" , font=("Comic Sans MS", "17", "bold"))
    login_password_label.place(relx=0.3, rely=0.3, anchor=CENTER)
    btn_login = Button(login, text="Log In" , width = 5, height = 2, font=("Comic Sans MS", "10",))
    btn_login.place(relx=0.5, rely=0.5, anchor=CENTER)
    
    