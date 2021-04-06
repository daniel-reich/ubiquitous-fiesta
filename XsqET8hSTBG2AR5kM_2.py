
def letter_distance(txt1, txt2):
  a = 'a b c d e f g h i j k l m n o p q r s t u v w x y z'.split()
  def l8r_dist(l1, l2, a):
    if l2 == 'A':
      return 32
    l1index = None
    l2index = None
    
    for n in range(26):
      tl8r = a[n]
      if tl8r == l1:
        l1index = n
      if tl8r == l2:
        l2index = n
      if l1index != None and l2index != None:
        break
    
    d = abs(l2index - l1index)
    
    return d
  
  txt_lengths = [len(txt1), len(txt2)]
  
  points = 0
  for n in range(0, min(txt_lengths)):
    
    tl1 = txt1[n]
    tl2 = txt2[n]
    
    if tl1 == tl2:
      points += 0
    else:
      points += l8r_dist(tl1, tl2, a)
  
  points += (max(txt_lengths) - min(txt_lengths))
  
  return points

