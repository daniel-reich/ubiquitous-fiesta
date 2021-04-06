
def letter_distance(txt1, txt2):
  return sum([abs(ord(i[1])-ord(i[0])) for i in zip(txt1,txt2)])+abs(len(txt1)-len(txt2))

