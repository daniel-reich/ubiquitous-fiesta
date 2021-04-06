
def modify(word):
    word = word.upper()[::-1]
    n = len(word)
    n2 = n // 2
    if n % 2 == 0:
        return word[:n2] + "-" + word[n2:]
    else:
        return word[:n2+1] + "-" + word[n2+1:]
    
def edit_words(lst):
    return [modify(w) for w in lst]

