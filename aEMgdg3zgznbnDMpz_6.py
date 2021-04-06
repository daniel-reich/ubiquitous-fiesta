
def rotated_words(txt):
  count=0
  txt=set(txt.split(' '))
  ruota={"H", "I", "N", "O", "S", "X", "Z",'W','M'}
  for x in txt:
    if set(x) and set(x)<=ruota:count+=1
  return count

