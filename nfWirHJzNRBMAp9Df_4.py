
def hamming_distance(txt1, txt2):
  return sum(a != b for a, b in zip(txt1, txt2))

