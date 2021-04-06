
def mirror_cipher(message,k="abcdefghijklmnopqrstuvwxyz"):
    table = k
    message = message.lower()
    return message.translate(str.maketrans(table,table[::-1]))

