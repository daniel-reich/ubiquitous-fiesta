
def censor_string(txt, lst, char):
    words = txt.split(" ")
    newtxt = [w if w not in lst else len(w)*char for w in words]
    return ' '.join(newtxt)

