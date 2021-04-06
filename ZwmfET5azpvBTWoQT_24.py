
def valid_word_nest(word, nest):
    while len(nest) > len(word):
        if nest.count(word) == 1:
            index = nest.index(word)
        else:
            return False
        nest = nest[ : index] + nest[index + len(word) : ]
    return word == nest

