from cryptography.fernet import Fernet
import os
import tkinter as tk
from tkinter import StringVar

#os.listdir() -> Returns a list of possible encrypt files and pass it back to the user
def get_files():
    files = [x for x in os.listdir() if (not x.endswith('.key')and x!= 'encrypt.py' and not x.endswith('.swp'))]
    return files

def get_bin_key(key_file):
    return open(key_file,'rb').read()

def get_keys():
    #Gets/Creates the key
    keys = [x for x in os.listdir() if x.endswith('.key')]
    return keys
    #with open(key_file,'rb') as file:

#Encrypt the specific file requested
#Can use either a new key or dropdown menu of keys
def encrypt(file_name,key_file):
    #TODO: add tkinter funcionality
    #starts the encryption process
    key = get_bin_key(key_file)
    #with open(key_file,'rb')as file:
    #key = get_keys()
    fernet = Fernet(key)
    with open(file_name,'rb') as file:
        org = file.read()
    if org[:len(magic)] == magic:
        raise ValueError('Already Encrypted')
    encrypted = fernet.encrypt(org)
    with open(file_name,'wb') as file:
        file.write(magic) #Writes the "magic" to check if encrypted
        file.write(encrypted)


#Decrypts the specific file requested
def decrypt(file_name,key_file):
    #TODO: Add tkinter functionality
    #starts the decryption process
    key = get_bin_key(key_file)
    fernet = Fernet(key)
    with open(file_name,'rb') as file:
        enc = file.read()
    if enc[:len(magic)] != magic:
        raise ValueError('Not encrypted') #Checks the magic to makesure encrypted
    enc = enc[len(magic):]
    decrypted = fernet.decrypt(enc)
    with open(file_name,'wb') as file:
        file.write(decrypted)


def start():
    user = input("(E)ncrypt or (D)ecrypt? -> ").lower()
    if user == 'e':
        encrypt('epic.txt')
    elif user == 'd':
        decrypt('epic.txt')
    else:
        print("Couldn't recognize try again")

def tkver():
    window.geometry("400x400")
    greeting = tk.Label(text="Hello, welcome to the encrypter")
    greeting.pack()
    #global enc_file_name,dec_file_name
    tkver.enc_file_name = "should not exist"
    #Ask which file to choose
    options = get_files()
    clicked = StringVar()
    clicked.set(options[-1])

    file_dropdown = tk.OptionMenu(window,clicked,*options)
    file_dropdown.pack()

    def file_clicked():
        file_label.config(text=clicked.get())
        tkver.enc_file_name = clicked.get()
        print(tkver.enc_file_name)
        key_start()
        #encrypt(clicked.get())
    def key_clicked():
        key_label.config(text=keys_clicked.get())
        tkver.enc_key_name = keys_clicked.get()
        print("key clicked")
        print(tkver.enc_file_name)
        choice_start()

    button = tk.Button(window,text = "Choose file",command = file_clicked).pack()
    file_label = tk.Label(window,text="")
    file_label.pack()
    key_label = tk.Label(window,text="")
    keys_clicked = StringVar()
    def key_start():
        #Ask what key file to do it with
        #TODO: Create a gui for a new key
        key_options = get_keys()
        keys_clicked.set(key_options[0])

        key_dropdown = tk.OptionMenu(window,keys_clicked,*key_options)
        key_dropdown.pack()

        btn = tk.Button(window,text = "Choose file", command = key_clicked).pack()
        key_label.pack()
    def choice_start():
        #Ask whether to encrypt or decrypt
        #Will use just 2 buttons side by side to determine
        print("choice_started")
        print(tkver.enc_file_name)
        enc_lmb = lambda : encrypt(tkver.enc_file_name,tkver.enc_key_name)
        dec_lmb = lambda : decrypt(tkver.enc_file_name,tkver.enc_key_name)
        enc_btn = tk.Button(window,text = "Encrypt",command = enc_lmb).pack()
        dec_btn = tk.Button(window,text = "Decrypt",command = dec_lmb).pack()
        #enc_dec

    window.mainloop()

if __name__ == "__main__":
    magic = b"xfaxc16mx9fxx1b"
    window = tk.Tk()
    tkver()
    #start()
