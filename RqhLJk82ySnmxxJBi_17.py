
def power_morphic(num):
  auto = lambda n, k: str(n) == str(n**k)[-len(str(n)):]
  morph = {0:'Amorphic', 1:'Enamorphic', 2:'Dimorphic', 4:'Quadrimorphic', 9:'Polymorphic'}
  return morph[sum(auto(num,i) for i in range(2,11))]

