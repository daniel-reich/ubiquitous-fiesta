
def same_vowel_group(w):
    vowel=["a","e","i","o","u"]
    vowelsfirstword=[letter for letter in w[0] if letter in vowel]
    vowelsnot=[letter for letter in vowel if letter not in vowelsfirstword]
    res=[w[0]]
    for word in w:
        for letter in word:
            if letter in vowelsfirstword and word not in res:
                res.append(word)
            elif letter in vowelsnot and word in res:
                res.remove(word)
                break
    return res

