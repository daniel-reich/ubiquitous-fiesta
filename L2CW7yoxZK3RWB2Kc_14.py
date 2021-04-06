
class Nico_Cypher:
​
  def __init__(self, key):
    self.k = key
    self.k_dic = {}
​
    s = sorted(key)
​
    for n in range(len(s)):
      if s[n] not in self.k_dic.keys():
        self.k_dic[s[n]] = [n+1]
      else:
        self.k_dic[s[n]].append(n+1)
    
    
​
  def encrypt(self, msg):
​
    lsts = []
    c = 0
​
    for l8r in msg:
      if len(lsts) < len(self.k):
        lsts.append([l8r])
      else:
        lsts[c%len(self.k)].append(l8r)
      c += 1
    
    goal = max([len(lst) for lst in lsts])
​
    for n in range(len(lsts)):
      lst = lsts[n]
      while len(lst) < goal:
        lst.append(' ')
      lsts[n] = lst
    
    l8r_indexes = {l8r:0 for l8r in set(self.k)}
    lst_indexes = {}
    lst_ind = 0
​
    for l8r in self.k:
      
      lst_indexes[self.k_dic[l8r][l8r_indexes[l8r]]] = lsts[lst_ind]
      l8r_indexes[l8r] += 1
      lst_ind += 1
    
    tr = ''
​
    for n in range(goal):
      for k in sorted(lst_indexes.keys()):
        tr += lst_indexes[k][n]
    
    return tr
def nico_cipher(msg, key):
  
  cypher = Nico_Cypher(key)
  return cypher.encrypt(msg)

