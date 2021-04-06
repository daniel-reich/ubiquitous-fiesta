
def nearest_vowel(s):
    dist = [(ch, abs(ord(s)-ord(ch))) for ch in 'aeiou']
    return sorted(dist, key=lambda tup:tup[1])[0][0]

