
def power_morphic(num):
  total = sum([str(num ** foo).endswith(str(num)) for foo in range(2, 10 + 1)])
  return "Polymorphic" if total == 9 else "Quadrimorphic" if total == 4 else "Dimorphic" if total == 2 else "Enamorphic" if total == 1 else "Amorphic"

