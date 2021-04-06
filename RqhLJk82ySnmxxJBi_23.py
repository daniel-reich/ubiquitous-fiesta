
def power_morphic(num):
  l = len([1 for x in range(2,11) if str(num**x)[-1*(len(str(num))):] == str(num)])
  n = ["Amorphic", "Enamorphic", "Dimorphic", "Quadrimorphic", "Polymorphic"]   
  return n[l] if l < 3 else n[3] if l == 4 else n[4]

