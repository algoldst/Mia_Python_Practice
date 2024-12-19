def encrypt(message: str):
    encrypted_message = ""
    for char in message:
        ascii_value = ord(char)
        ascii_value += 1
        encrypted_message += chr(ascii_value)
    return encrypted_message

def decrypt(encrypted_message: str):
    message = ""
    for char in encrypted_message:
        ascii_value = ord(char)
        ascii_value -= 1
        message += chr(ascii_value)
    return message
