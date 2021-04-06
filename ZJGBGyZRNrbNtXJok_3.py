
def nearest_vowel(s):
    return sorted([(abs(ord(s)-ord(x)), x) for x in 'aeiou'])[0][1]

