
def letter_distance(txt_1, txt_2):
  x = len(txt_1)
  y = len(txt_2)
  long = txt_1
  short = txt_2
  if y > x:
    short = txt_1
    long = txt_2
  total = len(long)- len(short)
  for i, letter in enumerate(short):
    total += abs(ord(short[i])-ord(long[i]))
  return total

