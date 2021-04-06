
from string import ascii_lowercase
def form_key(key):
    working_key = ""
    for letter in key + ascii_lowercase:
        if letter not in working_key:
            working_key += letter
    return working_key
def condi_cipher(message, key, shift):
    encode_key = form_key(key)
    encoded_msg = ""
    for letter in message:
        if letter not in encode_key:
            encoded_msg += letter
        else:
            encoded_msg += encode_key[(encode_key.index(letter) + shift) % 26]
            shift = encode_key.index(letter) + 1
    return encoded_msg

