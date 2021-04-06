
def valid_word_nest(word, nest):
    # print("word:",word)
    # print("nest:",nest)
    if len(nest) == len(word):
        if word == nest:
            return True
        else:
            return False
    elif len(nest) < len(word):
        return False
    else:
        if word in nest:
            if word*2 in nest:
                return False
            else:
                start = nest.find(word)
                end = start + len(word)
            return valid_word_nest(word, nest[:start] + nest[end:])
        else:
            return False

