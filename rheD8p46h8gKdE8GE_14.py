
def grayscale(lst):
  b = [[[k if 0<=k<=255 else 255 if k>255 else 0 for k in j]
     for j in i]for i in lst]
  a = []
  for i in b:
        a.append([[round(sum(j)/3)]*len(j) for j in i])
  return a

