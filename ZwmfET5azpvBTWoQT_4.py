
def valid_word_nest(word, nest):
    for i in range(int(len(nest)/len(word))):
        if len(nest) > len(nest.replace(word,'')) + len(word):
            return False
        nest = nest.replace(word,'')
    return False if len(nest)>0 else True

