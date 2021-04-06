
def get_quartiles(lst, method):
  lst.sort()
  q0, q2, q4 = lst[0], median(lst), lst[-1]
  if method == 'MS':
    q1 = lst[rnd((len(lst) + 1) / 4) - 1]
    q3 = lst[rnd(3 * (len(lst) + 1) / 4, False) - 1]
  else:
    if len(lst)%2 == 0: 
      sub1, sub2 = lst[:len(lst)//2], lst[len(lst)//2:]
    else:
      if method == 'T':
        sub1, sub2 = lst[:len(lst)//2 + 1], lst[len(lst)//2:]
      elif method == 'MM':
        sub1, sub2 = lst[:len(lst)//2], lst[len(lst)//2 + 1:]
    q1, q3 = median(sub1), median(sub2)
  return [q0, q1, q2, q3, q4]
  
def median(lst):
  return (lst[(len(lst)-1)//2] + lst[len(lst)//2]) / 2
  
def rnd(n, up=True):
  if n - int(n) < 0.5:
    return int(n)
  if n - int(n) > 0.5:
    return int(n) + 1
  else:
    return int(n) + 1 * up

