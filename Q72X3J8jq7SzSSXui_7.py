
def sentence_searcher(txt, word):
    txt = txt.split('.')
    for s in txt:
      if word.lower() in s.lower():
        return (s +'.').strip()
    return ''

