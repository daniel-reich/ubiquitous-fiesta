
def meme_sum(a, b):
  a, b = sorted([str(a), str(b)], key=len)
  
  res = ''
  for i, j in zip(a.zfill(len(b)), b):
    res += str(int(i) + int(j))
  return int(res)

