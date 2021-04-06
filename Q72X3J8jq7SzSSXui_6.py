
def sentence_searcher(txt, word):
  def sentence_splitter(sentence):
    return sentence.split('. ')
  
  sentences = sentence_splitter(txt)
  
  for sentence in sentences:
    if word.lower() in sentence.lower():
      return sentence + '.' if '.' not in sentence else sentence
  
  return ''

