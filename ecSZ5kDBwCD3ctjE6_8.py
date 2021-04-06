
def find_smallest_num(lst):
  sm = lst[0]
  for num in lst:
    if num < sm:
      sm = num
  return sm

