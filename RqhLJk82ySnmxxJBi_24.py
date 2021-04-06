
def power_morphic(num):
  count = sum([1 for k in range(2, 11) if str(num**k).endswith(str(num))])
  d = {0:'Amorphic', 1:'Enamorphic', 2:'Dimorphic', 4:'Quadrimorphic', 9:'Polymorphic'}
  return d.get(count)

