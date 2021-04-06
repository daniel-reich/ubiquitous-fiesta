
def hamming_distance(txt1, txt2):
  return sum(i != j for i,j in zip(txt1, txt2))

