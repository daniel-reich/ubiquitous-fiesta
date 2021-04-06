
def letter_distance(txt1, txt2):
  return sum([abs(ord(x)-ord(y)) for x,y in zip(txt1,txt2)])+abs(len(txt1)-len(txt2))

