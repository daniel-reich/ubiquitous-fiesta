
def sentence_searcher(txt, n):
    words = txt.split()
    i = 0
    lst = []
    for word in words:
        lst += [i]
        if word[-1] == '.':
            i += 1
    sentences = txt.split('.')
    return(sentences[lst[n]].strip() + '.')

