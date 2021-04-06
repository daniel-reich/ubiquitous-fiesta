
def letter_distance(txt1, txt2):
  ret = 0
  l1,l2 = len(txt1),len(txt2)
  for i in range(0,min(l1,l2)):
    ret+=abs(ord(txt1[i])-ord(txt2[i]))
  ret+=abs(l1-l2)
  return ret

