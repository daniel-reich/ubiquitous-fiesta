
def caesar_cipher(text, key):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    text_list = list(text.lower())
    alph = list(alphabet)
    encrypted  = []
    for i in range(len(text_list)):
        if text_list[i] != " ":
            encrypted.insert(i, alph[(alph.index(text_list[i]) + key) % 26])
        else:
            encrypted.insert(i, " ")
    return "".join(encrypted)

