
def letter_distance(txt1, txt2):
  return sum(abs(ord(txt1[i])-ord(txt2[i])) for i in range(min([len(txt1),len(txt2)]))) + abs(len(txt1)-len(txt2))

