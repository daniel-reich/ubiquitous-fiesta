
def valid_word_nest(word, nest):
    while nest:
        if nest.count(word) != 1:
            return False
        x = nest.find(word)
        if x == -1:
            return False
        nest = nest[:x] + nest[x+len(word):]
    return True

