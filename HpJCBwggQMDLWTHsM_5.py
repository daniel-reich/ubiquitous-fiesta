
def average_word_length(txt):
  totlgth = 0
  punctuation = ['(', ')', '?', ':', ':', ',', '.', '!', '/', '"', "'"]
  for i in punctuation:
    txt = txt.replace(i,"")
  splttxt = txt.split(' ')
  for wrd in splttxt:
    totlgth += len(wrd)
  return float('{:.2f}'.format(totlgth / len(splttxt)))

