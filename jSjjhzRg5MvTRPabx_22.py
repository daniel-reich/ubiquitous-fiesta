
def sentence(words):
    v = ['a','e','i','o','u']
    for i in range(len(words)):
        if words[i][0] in v:
            if i < len(words)-2:
                words[i] = 'an ' + words[i] + ','
            else:
                words[i] = 'an ' + words[i]
        else:
            if i < len(words)-2:
                words[i] = 'a ' + words[i] + ','
            else:
                words[i] = 'a ' + words[i]
    words[0] = words[0].capitalize()
​
    words[-1] = 'and ' + words[-1] + '.'
​
    return ' '.join(words)

