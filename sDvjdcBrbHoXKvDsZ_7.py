
def anagram(name, words):
    return sorted(name.lower())[1:] == sorted(''.join(words))

