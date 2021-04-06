
def map_letters(word):
    resultdict = {}
    for i in set(word):
       indxs = [j for j,ltr in enumerate(word) if ltr == i]
       resultdict[i] = indxs
    return resultdict

