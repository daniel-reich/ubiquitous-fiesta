
def power_morphic(n):
  s = str(n)
  d = {0:'Amorphic', 1:'Enamorphic', 2:'Dimorphic', 4:'Quadrimorphic', 9:'Polymorphic'}
  return d[sum(str(n**i).endswith(s) for i in range(2, 11))]

