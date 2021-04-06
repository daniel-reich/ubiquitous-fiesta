
def valid_word_nest(word, nest):
    while True:
        if word not in nest and nest != '' or nest.count(word) == 2:
            return False
        nest = nest.replace(word,'')
        if word == nest or nest == '':
            return True

