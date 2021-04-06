
def letter_distance(txt1, txt2):
  extra = abs(len(txt1) - len(txt2))
  return sum(abs(ord(a) - ord(b)) for a, b in zip(txt1, txt2)) + extra

