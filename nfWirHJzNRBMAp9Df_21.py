
def hamming_distance(txt1, txt2):
  count = 0
  for i,l in enumerate(txt1):
    if l != txt2[i]: count += 1
  return count

