
def embeded_within(txt, letters):
    return sorted({txt[s:e+1] for e in range(len(txt))
                for s in range(e+1)
                if txt[s] in letters and txt[e] in letters})
​
def get_vowel_substrings(txt):
    return embeded_within(txt, set('aeiou'))
def get_consonant_substrings(txt):
    return embeded_within(txt, set('bcdfghjklmnpqrstvwxyz'))

