
def missing(lst):
  dif=lst[1]-lst[0]
  for i in range(1,len(lst)):
    newdif = lst[i]-lst[i-1]
    if dif>newdif:
      return lst[i-1]-newdif
    if dif<newdif:
      return lst[i]-dif

