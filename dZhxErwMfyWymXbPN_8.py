
def hangman(phrase, lst):
    out = ['-' if letter.isalpha() else letter for letter in phrase]
    indicies = sorted([(x,y) for x,y in enumerate(phrase) for i in lst if i == y.lower()])
    for i in indicies:
        out[i[0]] = i[1]
    return "".join(out)

