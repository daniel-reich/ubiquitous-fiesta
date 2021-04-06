
def increasing_word_weights(sentence):
    for i in '.,?':
        sentence = sentence.replace(i, '')
    sentence = sentence.split()
    return [sum([ord(i) for i in y]) for y in sentence] == sorted([sum([ord(i) for i in y]) for y in sentence])

