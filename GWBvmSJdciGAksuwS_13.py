
def find_letters(word):
  res=[]
  for s in word:
    if word.count(s)==1:
      res.append(s)
  return res

