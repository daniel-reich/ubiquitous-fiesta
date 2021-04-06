
def find_letters(word):
  a=[]
  for i in word:
    if word.count(i)>1:
      pass
    else:
      a.append(i)
  return a

