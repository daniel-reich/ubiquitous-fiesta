
from re import match
def scrambled(words, mask):
    pat = mask.replace("*", r"\w") + "$"
    return [word for word in words if match(pat, word)]

