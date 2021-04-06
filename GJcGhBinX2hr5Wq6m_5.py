
def move_zeros(lst):
  z = lst.count(0)
  f = sum([1 for i in lst if str(i)=='False'])
  lst = [i for i in lst if str(i)=='False' or i!=0]
  [lst.append(0) for _ in range(z)]
  return lst[:-f] if f>0 else lst

