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
    supported_range = ord("z") - ord(" ") + 1 
    cipher = "" 
    for char in string:
        char_index = ord(char) - ord(" ")
        cipher = cipher + chr(ord(" ") + (char_index + shift) % supported_range)

    return cipher


def decrypt(string, shift):
    return encrypt(string, -shift)


def do_encrypt_test(test_string, expected_string, shift):
    if (encrypt(test_string, shift) == expected_string):
        print("PASS: Encryption test with shift {} passed".format(shift))
    else:
        print("FAILED: Encryption test with shift {} failed".format(shift))


def do_decrypt_test(test_string, expected_string, shift):
    if (decrypt(test_string, shift) == expected_string):
        print("PASS: Decryption test with shift {} passed".format(shift))
    else:
        print("FAILED: Decryption test with shift {} failed".format(shift))

def do_test():
    test_string = "ABC 123"
    encrypted_string_with_shift_1 = "BCD!234"
    encrypted_string_with_shift_2 = 'CDE"345'
    do_encrypt_test(test_string, encrypted_string_with_shift_1, 1)
    do_encrypt_test(test_string, encrypted_string_with_shift_2, 2)

    do_decrypt_test(encrypted_string_with_shift_1, test_string, 1)
    do_decrypt_test(encrypted_string_with_shift_2, test_string, 2)

    do_encrypt_test("z", " ", 1)
    do_decrypt_test(" ", "z", 1)

#Ask the user if they want to encrypt of decrypt
mode = input("Do you want to encript or decript?:")

#if e or encrypt Encrypt is true
#if d or decrypt Encrypt is false
#in neither then quit
if mode == "encrypt" or mode == "e":
    Encrypt = True
elif mode == "decrypt" or mode == "d":
    Encrypt = False
elif mode == "test" or mode == "t":
    do_test()
    exit(1)
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
    print("after decryption:", decrypt(text, shift_number))