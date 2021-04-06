
def avg(*args):
  args = [i for i in args if i!='i']
  return sum(args)/len(args)
def iqr(lst):
  lst = sorted(lst)
  l = len(lst)
  k = len(lst)%4//2-1
  return avg(lst[3*(l//4)+(l%4-1)],(lst[(3*(l//4)+l%4)] if abs(k) else 'i'))-avg(lst[l//4],(lst[l//4-1] if abs(k) else 'i'))

