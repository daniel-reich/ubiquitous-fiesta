
import re
​
def translate_sentence(sentence):
    res = []
​
    for word in sentence.split():
        if word[0].lower() in 'aeiou':
            pig = re.sub(r'(\w+)', r'\1' + 'yay', word)
        else:
            pig = re.sub(r'([^aeiou\W]+)(\w+)', r'\2\1' + 'ay', word)
        if any(i.isupper() for i in pig):
            pig = pig.title()
        res.append(pig)
​
    return ' '.join(res)
​
def translate_word(word):
    return translate_sentence(word)

