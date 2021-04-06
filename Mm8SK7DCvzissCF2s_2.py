
def is_alpha(word):
    myans = 0
    for item in word:
        a = ord(item.lower())
        if 97 <= a <= 122:
            myans += a - 96
    return myans % 2 == 0

