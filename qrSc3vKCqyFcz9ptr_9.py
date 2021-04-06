
def sum_round(num):
  lst = []
  
  while num > 0:
    num, r = divmod(num, 10)
    lst.append(r)
​
  return ' '.join(str(val*10**i) for i, val in enumerate(lst) if val > 0)

