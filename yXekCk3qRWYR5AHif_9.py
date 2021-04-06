
def vow_replace(word, vowel):
    set1 = set(['a','i','o','e','u'])
    for it1 in word:
        set2 = set(it1)
        if set2.issubset(set1):
            word = word.replace(it1, vowel)
    return word

