
def show_the_love(lst):
  minix = lst.index(min(lst))
  for i in range(len(lst)):
    if i != minix:
      lst[minix] += lst[i] / 4
      lst[i] -= lst[i] / 4
  return lst

