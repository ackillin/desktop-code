from cryptography.fernet import Fernet
import os
import tkinter as tk
from tkinter import StringVar

#os.listdir() -> Returns a list of possible encrypt files and pass it back to the user
def get_files():
    files = [x for x in os.listdir() if (not x.endswith('.key')and x!= 'encrypt.py' and not x.endswith('.swp'))]
    
    return files

def get_keys():
    #Gets/Creates the key
    keys = [x for x in os.listdir() if x.endswith('.key')]
    print(keys)
    key = open('filekey.key','rb').read()
    print(key)
    return key

#Encrypt the specific file requested
#Can use either a new key or dropdown menu of keys
def encrypt(file_name):
    #TODO: add tkinter funcionality
    #starts the encryption process
    key = get_keys()
    fernet = Fernet(key)
    with open(file_name,'rb') as file:
        org = file.read()
    encrypted = fernet.encrypt(org)
    with open(file_name,'wb') as file:
        file.write(encrypted)


#Decrypts the specific file requested
def decrypt(file_name):
    #TODO: Add tkinter functionality
    #starts the decryption process
    key = get_keys()
    fernet = Fernet(key)
    with open(file_name,'rb') as file:
        enc = file.read()
    decrypted = fernet.decrypt(enc)

    with open(file_name,'wb') as file:
        file.write(decrypted)


def start():
    user = input("(E)ncrypt or (D)ecrypt? -> ").lower()
    if user == 'e':
        encrypt('house.csv')
    elif user == 'd':
        decrypt('house.csv')
    else:
        print("Couldn't recognize try again")


def tkver():
    window.geometry("400x400")
    file_clicked = lambda : file_label.config(text=clicked.get())
    key_clicked = lambda : key_label.config(text=clicked.get())
    greeting = tk.Label(text="Hello, welcome to the encrypter")
    greeting.pack()
    #Ask which file to choose
    options = get_files()
    clicked = StringVar()
    clicked.set(options[0])

    file_dropdown = tk.OptionMenu(window,clicked,*options)
    file_dropdown.pack()

    button = tk.Button(window,text = "Choose file",command = file_clicked).pack()
    print("Label loaded")
    file_label = tk.Label(window,text="")
    file_label.pack()
    #Ask what key file to do it with
    #TODO: Create a gui for a new key
    #Ask whether to encrypt or decrypt
    #enc_dec
    window.mainloop()

if __name__ == "__main__":
    window = tk.Tk()
    tkver()
