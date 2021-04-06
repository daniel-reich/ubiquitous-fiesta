
def find_and_remove(dct):
  for x in dct:
    d1={}
    for y in dct[x]:
      if dct[x][y].isdigit():
        d1[y]=int(dct[x][y])
    dct[x]=d1
  return dct

