
def count_boomerangs(lst):
    return sum(
    i == k and i != j 
    for i, j, k in zip(lst, lst[1:], lst[2:])
  )

