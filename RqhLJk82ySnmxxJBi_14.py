
def power_morphic(num):
  dig = len(str(num))
  x = sum(1 for n in range(2, 11) if str(num**n)[-dig:] == str(num))
  n = "Poly" if x>4 else "Quadri" if x==4 else "Di" if x==2 else "Ena" if x==1 else "A"
  return "{}morphic".format(n)

