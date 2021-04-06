
def show_the_love(lst):
  sum = 0
  for i in lst:
    if i != min(lst):
      sum += i*0.25
  return [num*0.75 if num != min(lst) else num+sum for num in lst]

