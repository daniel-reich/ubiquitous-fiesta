
def letter_distance(txt1, txt2):
  return sum(abs(ord(i) - ord(j)) for i, j in zip(txt1, txt2)) + abs(len(txt1) - len(txt2))

