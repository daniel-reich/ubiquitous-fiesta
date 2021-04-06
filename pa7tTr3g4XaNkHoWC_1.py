
def pigLatin(w):
    if w[0] in 'aeiou':
        return w + 'way'
    for i, c in enumerate(w):
        if c in 'aeiou':
            return w[i:] + w[:i] + 'ay'
​
​
def pig_latin_sentence(sentence):
    return ' '.join(pigLatin(w) for w in sentence.split())

