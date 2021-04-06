
def dakiti(sentence):
    words = sentence.split()
    n = len(words)
    sentence = [""] * n
    for word in words:
        for k in range(1, 10):
            c = str(k)
            if c in word:
                sentence[k-1] = word.replace(c, '')
                break
    return ' '.join(sentence)

