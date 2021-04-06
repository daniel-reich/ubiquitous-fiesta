
def abbreviate(sentence, n=4):
  txt=''
  for word in sentence.split():
    if len(word)>=n:
      txt=txt+word[0].upper()
  return txt

