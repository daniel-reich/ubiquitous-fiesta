
def sentence_searcher(txt, n):
    l = len(txt.split())
    if n < 0:
        n += l
    s = -1
    for sent in txt.split('.'):
        s += len(sent.split())
        if s >= n:
            return sent.strip() + '.'

