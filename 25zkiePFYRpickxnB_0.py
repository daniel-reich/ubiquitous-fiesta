
def count_boomerangs(lst):
  return sum(lst[i-2]==lst[i]!=lst[i-1] for i in range(2,len(lst)))

