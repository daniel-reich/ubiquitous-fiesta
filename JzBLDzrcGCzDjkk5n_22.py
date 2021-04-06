
def encrypt(word):
    vows = {"a": 0, "e": 1, "i": 2, "o": 2, "u": 3, }
    out = ""
    for i in range(1, len(word) + 1):
        if word[-i] in vows:
            out = out + str(vows[word[-i]])
        else:
            out = out + str(word[-i])
    out = out + "aca"
    return out

