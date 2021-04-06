
def get_vowel_substrings(txt):
    vowels = 'aeiou'.strip(' ')
    if len(txt) == 1: 
        return [txt] if txt in vowels else []
​
    substrings = []
    for v,_ in enumerate(txt):
        if _ in vowels:
            substrings.append(_)
        else:
            continue
        if len(txt) == v+1:
            break
​
        for vmore,__ in enumerate(txt[v+1:]):
            if __ in vowels:
                substrings.append(''.join(txt[v:vmore+v+2]))
            else:
                continue
​
    substrings = list(set(substrings))
​
    if substrings.count('') :substrings.remove('')
    substrings = sorted(substrings)
    return substrings
​
​
​
def get_consonant_substrings(txt):
    consonants = ''.join(set('abcdefghijklmnopqrstuvwxyz') - set('aeiou'))
    if len(txt) == 1:
        return [txt] if txt in consonants else []
    substrings = []
    
    for v,_ in enumerate(txt):
        if _ in consonants:
            substrings.append(_)
        else:
            continue
        if len(txt) == v+1:
            break
        for vmore, __ in enumerate(txt[v+1:]):
            if __ in consonants:
                substrings.append(''.join(txt[v:vmore+v+2]))
            else:
                continue
    substrings = list(set(substrings))
    if substrings.count('') : substrings.remove('')
    substrings = sorted(substrings)
    return substrings

