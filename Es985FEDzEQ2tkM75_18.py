
def caesar_cipher(text, key):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    l = []
    for a in text:
        if a.isalpha():
            l.append(alphabet[(alphabet.index(a) + key) % 26])
        else:
            l.append(a)
    return ''.join(l)

