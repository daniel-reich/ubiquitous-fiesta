
def hamming_distance(txt1, txt2):
  return sum(t1 != t2 for t1, t2 in zip(txt1, txt2))

