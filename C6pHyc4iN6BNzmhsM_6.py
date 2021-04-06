
def poker_hand_ranking(deck):
  import re
  d={'J':12,'Q':13,'K':14,"A":11}
  res=[re.sub( r"([a-z])", r" \1", s).split() \
  for s in [str(d[i[0]])+ i[1] if i[0] in 'JQKA' else i for i in deck]]
  tmp = sorted([int(row[0]) for row in res])
  tmp_= sorted([int(row[0]) for row in res])
  tmp1= list(set(tmp))
  if (sorted([10,11,12,13,14]) == sorted(tmp) and len(set([row[1] \
  for row in res]))==1):
    return('Royal Flush')
  elif (len(set(sorted(tmp)))==5 and len(set([row[1] for row in res]))==1):
    if tmp[0] == tmp[1]-1 and tmp[1]==tmp[2]-1 and tmp[2]==tmp[3]-1\
    and tmp[3] == tmp[4]-1:
      return('Straight Flush')
    else:
      if not(tmp.count(list(set(tmp))[0])==4 or \
      tmp.count(list(set(tmp))[1])==4):
        return('Flush')
  elif (len(set(sorted(tmp)))<=2):
    if tmp.count(list(set(tmp))[0])==4 or \
    tmp.count(list(set(tmp))[1])==4 :
      return('Four of a Kind')
    else:
      return('Full House')
  elif (len(set(sorted(tmp)))==5 and not len(set([row[1] \
  for row in res]))==1):
    if tmp[0] == tmp[1]-1 and tmp[1]==tmp[2]-1 and tmp[2]==tmp[3]-1 and\
    tmp[3] == tmp[4]-1:
      return('Straight')
    else:
      return ("High Card")
  elif (len(set(sorted(tmp)))<=3):
    if tmp.count(tmp1[0])==3 or tmp.count(tmp1[1])==3 or  \
    tmp.count(tmp1[2])==3:
      return('Three of a Kind')
    else:
      return('Two Pair')
  elif (len(set(sorted(tmp)))==4):
    return('Pair')

