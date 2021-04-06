
def caesar_cipher(text, key):
    al = "abcdefghijklmnopqrstuvwxyz"
    sol = ''
   
    for char in text:
        if char.islower():
            sol = sol + al[(al.find(char) + key) % 26]
        elif char.isupper():
            sol = sol + al[(al.find(char.lower()) + key) % 26].upper()
        else: sol += char
    return sol

