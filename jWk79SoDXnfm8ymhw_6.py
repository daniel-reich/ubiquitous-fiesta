
def star(word):
    return word.replace(word, len(word) * '*')
​
​
def censor(sentence):
    modified = [
        star(word)
        if len(word) > 4
        else word
        for word in sentence.split()
    ]
    return ' '.join(modified)

