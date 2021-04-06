
def sentence_searcher(txt, word):
  split_sentence = txt.split('.')
  for eachsentence in split_sentence:
    if word.lower() in eachsentence.lower():
      return eachsentence.strip() + "."
  return ''

