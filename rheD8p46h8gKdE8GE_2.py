
def grayscale(lst):
  res = [[]]
  for x in lst:
    for y in x:
      range_correct = [num if num<256 else 255 for num in y]
      temp = [round(sum(range_correct)/3) if sum(range_correct)>0 else 0]*3
      if len(res[-1])<len(x):       
        res[-1].append(temp)
      else:
        res.append([temp])
  return res

