
def remove_vowels(txt):
    vowels=("a","e","i","o","u","A","E","I","O","U")
    for elem in vowels:
        if elem in txt:
            txt=txt.replace(elem,"")
    return txt

