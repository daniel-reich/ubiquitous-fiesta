
def hamming_distance(txt1, txt2):
  return sum(1 for i in range(len(txt1)) if txt1[i]!=txt2[i])

