
def hamming_distance(txt1, txt2):
  n=0
  for i,x in zip(txt1, txt2):
    if i != x:
      n+=1
  return n

