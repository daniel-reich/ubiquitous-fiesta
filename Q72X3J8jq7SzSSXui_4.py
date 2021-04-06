
def sentence_searcher(txt, word):
    if word.lower() not in txt.lower():
        return ''
​
    for s in txt.lower().split('.'):
        if word.lower() in s:
            return (s.strip() + '.').capitalize()

