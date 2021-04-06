
def same_vowel_group(w):
    def vowels(w, f):
        return set([x for x in w if x in 'aeiou']) == set([y for y in f if y in 'aeiou'])
​
    return [x for x in w if vowels(x, w[0])]

