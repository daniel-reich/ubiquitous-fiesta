
def missing_letter(string):
    alphabet, missing = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
                        "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"], []
    for i in range(alphabet.index(string[0]), alphabet.index(string[-1])+1):
        if alphabet[i] in string:
            continue
        missing = alphabet[i]
    return missing if len(missing) != 0 else "No Missing Letter"

