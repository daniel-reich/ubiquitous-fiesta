
from collections import Counter
​
def hidden_anagram(text, phrase):
    text = ''.join([c for c in text.lower() if c.isalpha()])
    phrase = ''.join([c for c in phrase.lower() if c.isalpha()])
    lp, lt = len(phrase), len(text)
    if lp > lt:
        return 'noutfond'
    chunk = text[:lp]
    Ct = Counter(chunk)
    Cp = Counter(phrase)
    if Ct == Cp:
        return chunk
    for c in text[lp:]:
        chunk = chunk[1:] + c
        Ct = Counter(chunk)
        if Ct == Cp:
            return chunk
    return 'noutfond'

