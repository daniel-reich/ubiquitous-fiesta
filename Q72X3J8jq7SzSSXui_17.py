
def sentence_searcher(txt, word):
  sentences = txt.split('. ')
  for sentence in sentences:
    if word.lower() in sentence.lower(): 
      if '.' in sentence: return sentence
      return sentence + '.'
  return ''

