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

Encrypt = False  #Define all the variables
string = ""
shift = 0

#definging encrypt
#supported_range is the range that the cipher supports
def encrypt(string, shift):
    supported_range = ord("z") - ord(" ")
    cipher = "" 
    for char in string:
        char_index = ord(char) - ord(" ")
        cipher = cipher + chr(ord(" ") + (char_index + shift) % supported_range)

    return cipher

#Ask the user if they want to encrypt of decrypt
mode = input("Do you want to encript or decript?:")

#if e or encrypt Encrypt is true
#if d or decrypt Encrypt is false
#in neither then quit
if mode == "encrypt" or mode == "e":
    Encrypt = True
elif mode == "decrypt" or mode == "d":
    Encrypt = False
else:
    print("Incorrect mode")
    exit(1)
#if encrypt is true
#ask shift number
if Encrypt:
    text = input("enter text:")
    shift_number = int(input("enter shift number:"))
    print("original text:", text)
    print("after encryption:", encrypt(text, shift_number))
#else (encypt is false)
#ask shift number
#shift_number becomes negative
else:
    text = input("enter encrypted text: ")
    shift_number = int(input("enter shift number: "))
    shift_number = -shift_number
    print("after decryption:", encrypt(text, shift_number))
