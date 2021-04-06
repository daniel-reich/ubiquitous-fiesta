
def hamming_distance(txt1, txt2):
  return sum([1 for x, y in zip(txt1, txt2) if x != y])

