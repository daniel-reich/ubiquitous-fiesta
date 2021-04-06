
def pos_neg_sort(lst):
  def pos_neg_seperator(l):
​
    neg_dic = {}
    pos = []
​
    for number in range(0, len(l)):
​
      item = l[number]
      if item > 0:
        pos.append(item)
      else:
        neg_dic[number] = item
    
    return neg_dic,  sorted(pos)
  def sort_them(nd, p, length):
    nl = []
​
    for number in range(0, l):
      if number in nd:
        nl.append(nd[number])
      else:
        nl.append(p[0])
        p.pop(0)
    
    return nl
​
  
  pns = pos_neg_seperator(lst)
​
  nd = pns[0]
  pos = pns[1]
  l = len(lst)
​
  sortd = sort_them(nd, pos, l)
​
  return sortd

