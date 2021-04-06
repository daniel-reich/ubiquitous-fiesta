
def hamming_distance(txt1, txt2):
  hamming = 0
  for x in range (0, len(txt1)):
    if txt1[x] != txt2[x]:
      hamming+= 1
  return hamming

