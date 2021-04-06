
import re
​
def encrypt(key, message):
    return(message.translate(str.maketrans(key[::-1], re.sub("(.)(.)", r"\2\1", key[::-1]))))

