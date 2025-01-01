# DON"T TOUCH THIS FILE!
# DON"T EVEN LOOK AT IT!
# Okay I'm kidding, you can look at it.
# But don't use it please. :)
# It contains all the secrets of my love for you,
# which will be revealed in due time. :) ❤ ❤ ❤

def encrypt(message: str):
    encrypted_message = ""
    for char in message:
        ascii_value = ord(char)
        ascii_value += 10
        encrypted_message += chr(ascii_value)
    return encrypted_message

def decrypt(encrypted_message: str):
    message = ""
    for char in encrypted_message:
        ascii_value = ord(char)
        ascii_value -= 10
        message += chr(ascii_value)
    return message

def title_sequence(title: str):
    dashes = '----'
    for char in title:
        dashes += '-'
    
    print("\n")
    print("|" + dashes + "|")
    print("|  " + title + "  |")
    print("|" + dashes + "|")
