
def censor(s):
    return ' '.join([word.replace(word, '*'*len(word)) if len(word) > 4 else word for word in s.split()])

