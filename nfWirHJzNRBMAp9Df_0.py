
def hamming_distance(txt1, txt2):
  return sum(x!=y for (x,y) in zip(txt1,txt2))

