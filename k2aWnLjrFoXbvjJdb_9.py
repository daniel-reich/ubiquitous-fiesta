
def vigenere(text, keyword):
    keyword = ("").join([char for char in keyword.upper() if char.isalpha()])
    cyphert = [char for char in text.upper() if char.isalpha()]
    x=0
    while len(keyword) < len(cyphert):
        keyword += keyword[x]
        x += 1
    if text == "".join([char for char in text.upper() if char.isalpha()]):
        for y in range(len(cyphert)):
            cyphert[y] = chr((((ord(cyphert[y])-65)-(ord(keyword[y])-65))%26)+65)
    else:
        for y in range(len(cyphert)):
            cyphert[y] = chr((((ord(cyphert[y])-65)+(ord(keyword[y])-65))%26)+65)
    return("".join(cyphert))

