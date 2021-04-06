
def show_the_love(lst):
  minimum = lst.index(min(lst))
  for i in range(len(lst)):
    if lst[i] != lst[minimum]:
      addition = lst[i] * 0.25
      lst[i] = lst[i] - addition
      lst[minimum] = lst[minimum] + addition
  return lst

