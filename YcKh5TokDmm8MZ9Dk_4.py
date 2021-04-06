
from string import punctuation
from collections import Counter
​
def clean(text):
    return text.lower().translate(str.maketrans('', '', punctuation + ' '))
def hidden_anagram(text, phrase):
    phrase = clean(phrase)    
    text = ''.join(filter(str.isalpha, clean(text)))
    start = end = flag =0
    out, a = text, Counter(phrase)
    
    while start < len(text):
        if end < len(text) and end-start+1 < len(phrase):
            end += 1
        else:
            if not a - Counter(text[start:end+1]):
                out = min(out, text[start:end+1], key=len)
                flag = True
            start += 1
    return out if flag else 'noutfond'

