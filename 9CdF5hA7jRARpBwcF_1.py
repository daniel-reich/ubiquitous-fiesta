
def map_letters(word):
    d = {}
    for idx, letter in enumerate(word):
        if letter in d:
            d[letter].append(idx)
        else:
            d[letter] = [idx]
    return d

