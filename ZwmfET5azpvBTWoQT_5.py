
def valid_word_nest(word, nest):
    while word in nest:
        if word == nest:
            return True
        nest = nest.split(word)[0]+nest.split(word)[1]
    return False

