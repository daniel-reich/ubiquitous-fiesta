
import re
​
def pig_latin_sentence(sentence):
    res = []
    for s in sentence.split():
        if s[0] in 'aeiou':
             res.append(s + 'way')
        else:
            res.append(re.sub(r'([^aeiou]+)([aeiou].+)', r'\2\1ay', s))
    return ' '.join(res)

