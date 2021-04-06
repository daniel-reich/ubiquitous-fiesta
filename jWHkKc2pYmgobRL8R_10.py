
def distance_to_nearest_vowel(txt):
    i = 0 
    vowels = []
    for c in txt:
        if c in 'aeiou':
            vowels += [txt.index(c, i)]
        i += 1
    i -= i
    distance = []
    for c in txt:
        distance += [abs(i - min(vowels, key=lambda x: abs(x-i)))]
        i += 1
    return distance

