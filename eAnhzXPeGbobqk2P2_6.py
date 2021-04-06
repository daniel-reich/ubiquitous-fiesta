
def century(year):
  word=str(year)
  l1=word[0:2]
  cen=int(l1)+1
  if year>2000:
    return str(cen)+"st century"
  if word[1:4]=="000":
    return word[0:2]+"th century"
  else:
    return str(cen)+"th century"

