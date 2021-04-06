
def uncensor(txt, vowels):
    positions = [x for x,y in enumerate(txt) if y == "*"]
    list_txt = list(txt)
    for i in range(0,len(vowels)):
        list_txt[positions[i]] = vowels[i]
    return "".join(list_txt)

