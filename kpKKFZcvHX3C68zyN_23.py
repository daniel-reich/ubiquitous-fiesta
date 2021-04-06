
def swap_cards(n1, n2):
  s1,s2=list(map(int,str(n1))),list(map(int,str(n2)))
  if len(set(s1))==1 or min(s1)==s1[0]:
    return int("{}{}".format(s2[0],s1[1]))>int("{}{}".format(s1[0],s2[1]))
  return int("{}{}".format(s1[0],s2[0]))>int("{}{}".format(s1[1],s2[1]))

