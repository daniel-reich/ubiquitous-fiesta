
def valid_word_nest(word, nest):
    while nest:
        if word in nest and nest.count(word) == 1:
            nest = nest.replace(word, '')
        else:
            return False
    return True

