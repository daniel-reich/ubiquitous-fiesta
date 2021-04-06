
def get_vowel_substrings(txt):
    sov = set()
    for i, x in enumerate(txt):
        if x in 'aeiou':
            for j in range(i, len(txt)):
                if txt[j] in 'aeiou':
                    sov.add(txt[i:j+1])
    return sorted(sov)
                              
def get_consonant_substrings(txt):
    soc = set()
    for i, x in enumerate(txt):
        if x not in 'aeiou':
            for j in range(i, len(txt)):
                if txt[j] not in 'aeiou':
                    soc.add(txt[i:j+1])
    return sorted(soc)

