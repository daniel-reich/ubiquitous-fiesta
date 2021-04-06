
def sentence_searcher(txt, word):
  sentences = txt.split('. ')
  for sentence in sentences:
    if word.lower() in sentence.lower():
      return sentence if sentence[-1] == '.' else sentence + '.'
  return ''

