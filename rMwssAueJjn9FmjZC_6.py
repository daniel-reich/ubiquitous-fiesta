
def number_pairs(txt):
  A=txt[1:].split()
  return sum(A.count(x)//2 for x in set(A))

