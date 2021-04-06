
def sentence_searcher(txt, word):
    try:
        return [i.lstrip() + '.' for i in txt.split('.')[:-1] if word.lower() in i.lower()][0]
    except IndexError:
        return ''

