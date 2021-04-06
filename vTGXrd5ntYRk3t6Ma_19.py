
def is_isogram(txt):
  txt=txt.lower()
  return all(txt.count(i)==1 for i in txt)

