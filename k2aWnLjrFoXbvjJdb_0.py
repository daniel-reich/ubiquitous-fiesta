
tableau = [[chr(i) for i in range(65, 91)]]
for k in range(25):
    last = tableau[-1]
    tableau.append(last[1:] + last[:1])
​
def vigenere_encrypt(keyword, message):
    keyword = keyword.upper()
    message = message.upper()
    l = len(keyword)
    encrypted = ""
    for k in range(len(message)):
        key = keyword[k % l]
        row = ord(key) - 65
        column = ord(message[k]) - 65
        encrypted += tableau[row][column]
    return encrypted
​
def vigenere_decrypt(keyword, encrypted):
    keyword = keyword.upper()
    encrypted = encrypted.upper()    
    l = len(keyword)
    message = ""
    for k in range(len(encrypted)):
        key = keyword[k % l]
        row = ord(key) - 65
        column = tableau[row].index(encrypted[k])
        message += tableau[0][column]
    return message
​
def vigenere(text, keyword):
    if all(['A' <= char <= 'Z' for char in text]):
        return vigenere_decrypt(keyword, text)
    else:
        text = ''.join([t for t in text.upper() if 'A' <= t <= 'Z'])
        return vigenere_encrypt(keyword, text)

