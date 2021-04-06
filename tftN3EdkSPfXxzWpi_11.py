
def sentence_searcher(txt, n):
    num_of_words = txt.count(' ') + 1
    if n < 0:
        n += num_of_words
    sentences = [i.lstrip() for i in txt.split('.')[:-1]]
    pos = 0
​
    for sentence in sentences:
        for word in sentence.split():
            if pos == n:
                return sentence + '.'
            pos += 1

