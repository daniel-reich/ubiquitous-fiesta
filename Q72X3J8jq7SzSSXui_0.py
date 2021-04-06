
def sentence_searcher(txt, word):
  txt = txt.split('.')
  for i in txt:
    if word.lower() in i.lower():
      return i.strip()+'.'
  return ''

