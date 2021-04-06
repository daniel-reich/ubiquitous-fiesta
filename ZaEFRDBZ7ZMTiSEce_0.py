
def find_nemo(sentence):
    s=sentence.split()
    if 'Nemo' in s:
        return 'I found Nemo at {}!'.format(s.index('Nemo')+1)
    return "I can't find Nemo :("

