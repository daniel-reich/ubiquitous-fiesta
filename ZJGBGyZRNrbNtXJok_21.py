
def nearest_vowel(s):
    return sorted(('a', 'e', 'i', 'o', 'u'), key=lambda x: abs(ord(x)-ord(s)))[0]

