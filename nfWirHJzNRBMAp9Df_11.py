
def hamming_distance(txt1, txt2):
  k = 0
  a = len(txt1)
  for i in range(a):
    k += txt1[i] != txt2[i]
  return k;

