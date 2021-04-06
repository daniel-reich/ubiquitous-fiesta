
def get_lucky_number(size, nth):
  x,lst = 2,list(range(1,size+1))
  while x <= len(lst):
    lst = [i for i in lst if lst.index(i) % x != x - 1]
    x = lst[lst.index(x)+1 if x in lst else 1]
  return lst[nth-1]

