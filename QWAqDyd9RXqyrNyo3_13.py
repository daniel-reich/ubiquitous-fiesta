
def abbreviate(sentence, n=4):
  return ''.join(i[0] for i in sentence.upper().split() if len(i)>=n)

