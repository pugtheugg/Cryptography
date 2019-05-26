'''
from tkinter import *

window = Tk()

window.title("SECRET CODE MAKER")

window.geometry('350x200')

lbl = Label(window)

lbl.grid(column=0, row=0)



def clicked():
    lbl.configure(text="Button was clicked !!")


btn = Button(window, text="Encrypt", command=clicked)

btn.grid(column=1, row=0)

window.mainloop()
'''

Encrypt = False
Decrypt = False
string = ""
shift = 0


def encrypt(string, shift):
    cipher = ""
    for char in string:
        if char == " ":
            cipher = cipher + char
        elif char.isupper():
            cipher = cipher + chr((ord(char) + shift - 65) % 26 + 65)
        else:
            cipher = cipher + chr((ord(char) + shift - 97) % 26 + 97)

    return cipher


mode = input("Do you want to encript or decript?: ")

if mode == "encript" or mode == "e":
    encrypt(string, shift)
    Encrypt = True

if mode == "d":
    encrypt(string, shift)
    Decrypt = True

if Encrypt == True:
    text = input("enter text: ")
    shift_number = int(input("enter shift number: "))
    print("original text: ", text)
    print("after encryption: ", encrypt(text, shift_number))

if Decrypt == True:
    text = input("enter text: ")
    shift_number = int(input("enter shift number: "))
    shift_number = -shift_number
    print("after decryption: ", encrypt(text, shift_number))
