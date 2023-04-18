#Ken Leam G. Gamboa
#BSCPE 1-5
#Creating a Vigenere Cipher program 

import time
import pyfiglet

#create a dictionary translating each character to their corresponding numerical value, and vice versa
TEXT_TO_NUM = {'A':0,'B':1,'C':2,'D':3,'E':4,'F':5,'G':6,'H':7,'I':8,'J':9,'K':10,'L':11,'M':12,'N':13,'O':14,'P':15,'Q':16,'R':17,'S':18,'T':19,'U':20,'V':21,'W':22,'X':23,'Y':24,'Z':25}
NUM_TO_TEXT = {0:'A',1:'B',2:'C',3:'D',4:'E',5:'F',6:'G',7:'H',8:'I',9:'J',10:'K',11:'L',12:'M',13:'N',14:'O',15:'P',16:'Q',17:'R',18:'S',19:'T',20:'U',21:'V',22:'W',23:'X',24:'Y',25:'Z'}

#create a function that has the message and key as its parameters used for encryption
def encrypt_message(message, key):
    ciphertext = ""
    index = 0
    #convert each character in the message and key into their corresponding numerical values
    for characters in message:
        #convert each character in the message to numbers from 0-25 according to the dictionary
        if characters.isalpha():
            convert_to_num = TEXT_TO_NUM[characters]
        #convert each character in the key to numbers from 0-25
            key_in_num = TEXT_TO_NUM[key[index]]
        #add both values, then mod 26
            convert_to_num = (convert_to_num + key_in_num) % 26
        #revert the numerical value back into text
            convert_to_char = NUM_TO_TEXT[convert_to_num]
        #append new characters into ciphertext
            ciphertext += convert_to_char
        #proceed to the next character of key
            index = (index + 1) % len(key)
        #in case there are non-alphabet caharacters, append to the ciphertext
        else:
            ciphertext += characters
    return ciphertext

#create title design and introduction of the program
TITLE = "Vigenere Cipher"
time.sleep(2)
print("\033[94m" + "\033[1m" + pyfiglet.figlet_format(TITLE.center(50), font = "contessa"))
time.sleep(1)
print("Hello! This program is designed to encrypt the message inputted by the user in accordance with its inputted key.\n")
#ask for user's input

#call out the function
#print the ciphertext
#ask user if they want try again
    #if yes, repeat the program
    #if no, break
    #else, prompt invalid input then ask user to try again
#create program ender

