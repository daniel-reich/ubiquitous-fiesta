
def sentence_searcher(txt, word):
  lst = ([i for i in txt.split('.') if (word.lower()) in i.lower().split()])
  return '' if not lst else lst[0].strip() + '.'

