
def caesar_cipher(text, key):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    return ''.join((alphabet[(alphabet.index(c) + key) % 26]
                    if c in alphabet else c) for c in text)

