
def mirror_cipher(message, key = "abcdefghijklmnopqrstuvwxyz"):
    encoded_message = ""
    for let in message.lower():
        if let in key:
            cur_i = (key.index(let)+1) * -1
            encoded_message +=key[cur_i]
        else:
            encoded_message += let
    return encoded_message

