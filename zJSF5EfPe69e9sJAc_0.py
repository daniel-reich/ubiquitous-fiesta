
def censor_string(txt, lst, character):
    for word in lst:
        txt = txt.replace(word, character*len(word))
    return txt

