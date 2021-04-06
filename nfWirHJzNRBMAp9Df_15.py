
def hamming_distance(txt1, txt2):
  hum = 0
  for i in range(len(txt1)):
    if txt1[i] != txt2[i]:
      hum += 1
  return hum

