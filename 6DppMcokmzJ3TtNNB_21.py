
def true_alphabetic(txt):
    lst, res = txt.split(), []
    letters = sorted(c for word in lst for c in word)
    for word in lst:
        res.append(''.join(letters[:len(word)]))
        letters = letters[len(word):]
    return ' '.join(res)

