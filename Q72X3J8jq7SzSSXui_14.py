
def sentence_searcher(txt, word):
  sentences = txt.split(".")
  for x in sentences:
    print(word.lower())
    print(x)
    if word.lower() in x.lower():
      return x+'.' if x[0] != ' ' else x[1::]+'.'
  return ''

