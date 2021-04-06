
from random import randint
def numbers():
    num = ""
    while len(num)<5:
        temp = str(randint(1,5))
        if temp not in num:
            num += temp
    return int(num)

