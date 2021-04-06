
def hamming_distance(txt1, txt2):
  res = 0
  for i in range(len(txt1)):
    if txt1[i] != txt2[i]: res += 1
  return res

