
def map_letters(word):
    mapping = {}
    for index, letter in enumerate(word):
        if letter in mapping:
            mapping[letter] += [index]
        else:
            mapping[letter] = [index]
    return mapping

