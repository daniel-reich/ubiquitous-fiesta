
def syllabification(word):
    '''
    Returns a syllabificated version of words as per the instructions.
    '''
    s_word = ''
    i = len(word) - 1  # step backwards through word
    VOWELS = {'A', 'a', 'e', 'i', 'o', 'u'} # the Persian vowels
​
    while i >= 0:
        if word[i] not in VOWELS:
            s_word = word[i] + s_word
            i-= 1
        else:
            s_word = '.' + word[i-1] + word[i] + s_word
            i-= 2  # skip over CV
​
    return s_word[1:]  # drop the leading '.'

