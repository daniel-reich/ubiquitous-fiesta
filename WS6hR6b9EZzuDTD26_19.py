
def no_duplicate_letters(phrase):
    l = phrase.split()
    for word in l:
        for letter in set(word):
            if word.count(letter) > 1:
                return False
    return True

