
def valid_word_nest(word, nest):
    if nest.count(word)>1: return False
    while len(nest)>len(word):
        for i in range(0, len(nest)):
            if nest[i:i+len(word)]==word:
                return valid_word_nest(word, nest[:i] + nest[i+len(word):])
        return False
    return word == nest

