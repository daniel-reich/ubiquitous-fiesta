
def anagram(name, words):
    '''
    Returns whether the letters in words form an anagram of those in name
    '''
    return sorted(l for l in name.lower() if l.isalpha()) == sorted(''.join(words))

