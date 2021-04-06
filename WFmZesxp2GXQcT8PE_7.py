
def digital_cipher(message, key):
    while len(str(key)) < len(message):
        key = str(key) + str(key)
    return [ord(message[i]) + int(str(key)[i]) - 96 for i in range(len(message))]

