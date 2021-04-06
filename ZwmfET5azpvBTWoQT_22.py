
def valid_word_nest(word, nest):
    while word in nest:
        if nest.count(word) > 1:
            return False
        nest = nest.replace(word,"")
    return nest == ""

