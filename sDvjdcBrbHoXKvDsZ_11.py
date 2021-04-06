
def anagram(s, l):
    return sorted(s.replace(' ', '').lower()) == sorted(''.join(l))

