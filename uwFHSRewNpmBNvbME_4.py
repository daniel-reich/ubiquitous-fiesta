
def same_vowel_group(w):
    v = 'aeiou'
    return [j for j in w if set(i for i in j if i in v) == set(i for i in w[0] if i in v)]

