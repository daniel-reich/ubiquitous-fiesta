
def find_nemo(sentence):
    for idx, i in enumerate(sentence.split(), 1):
        if i == 'Nemo':
            return "I found Nemo at {}!".format(idx)
    return "I can't find Nemo :("

