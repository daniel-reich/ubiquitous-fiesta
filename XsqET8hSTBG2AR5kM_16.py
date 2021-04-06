
def letter_distance(txt1, txt2):
  return sum(abs(ord(a)-ord(b)) for a,b in zip(txt1, txt2)) + \
    (abs(len(txt1)-len(txt2)) if len(txt1) != len(txt2) else 0)

