
def letter_distance(txt1, txt2):
  if len(txt1) > len(txt2):
    n = len(txt2)
  else:
    n = len(txt1)
  return sum(abs(ord(txt1[i]) - ord(txt2[i])) for i in range(n)) + abs(len(txt1) - len(txt2))

