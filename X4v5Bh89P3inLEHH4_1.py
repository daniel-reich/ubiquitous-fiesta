
def spin_around(lst):
  D = {'right':.25, 'left':-.25}
  return abs(sum(D[i] for i in lst))//1

