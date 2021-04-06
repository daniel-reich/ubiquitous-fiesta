
def is_slidey(num):
  num = str(num);
  return all([abs(int(a) - int(b)) == 1 for (a,b) in zip(num , num[1:])])

