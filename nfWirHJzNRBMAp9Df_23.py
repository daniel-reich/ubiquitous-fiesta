
def hamming_distance(txt1, txt2):
  a = [txt1, txt2]
  return sum([int(a[0][i] != a[1][i]) for i in range(len(a[0]))])

