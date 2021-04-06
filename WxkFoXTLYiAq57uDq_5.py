
def find_and_remove(dct):
  for i in dct:
    dct[i] = dict([[j,int(dct[i][j])] for j in dct[i] if dct[i][j].isdigit()])
  return dct

