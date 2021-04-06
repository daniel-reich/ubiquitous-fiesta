
def sentence_searcher(txt, word):
  txt=txt[:-1]
  A=txt.split('. ')
  B=[]
  for x in A:
    if word.lower() in x.lower():
      B.append(x+'.')
  if B:
    return B[0]
  else:
    return ''

