
def grayscale(lst):
  l = lst
  for i in l:
    for j in i:
      summation = 0
      for k in range(len(j)):
        if j[k] < 0:
          j[k]=0
        elif j[k] > 255:
          j[k]=255
        summation+=j[k]
      avg = round(summation/(k+1))
      for m in range(len(j)):
        j[m] = avg
  return l

