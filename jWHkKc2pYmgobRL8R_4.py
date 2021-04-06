
def distance_to_nearest_vowel(txt):
    return list(map(lambda x:min(abs(x-i) for i in list(filter(lambda x:txt[x] in 'aeiou',range(len(txt))))),range(len(txt))))

