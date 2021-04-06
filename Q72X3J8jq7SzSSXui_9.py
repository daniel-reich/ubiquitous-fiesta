
def sentence_searcher(txt, word):
    for sent in txt.split('.'):
        if word.lower() in sent.lower():
            return sent.strip() + '.'
    return ""

