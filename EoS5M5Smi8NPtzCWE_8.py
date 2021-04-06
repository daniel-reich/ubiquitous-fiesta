
def secret(text):
    front = text[:(len(text)-2)]
    return ("<" + front + "></" + front + ">") * int(text[len(text)-1])

