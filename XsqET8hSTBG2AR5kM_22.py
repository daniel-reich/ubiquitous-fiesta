
def letter_distance(txt1, txt2):
  a = [str(x) for x in txt1]
  b = [str(x) for x in txt2]
  c = [abs(ord(x)-ord(y)) for x, y in zip(a, b)]
  return sum(c)+abs(len(txt1)-len(txt2))

