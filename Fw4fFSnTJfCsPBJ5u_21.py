
def how_many_missing(lst):
  if len(lst)==0:return 0
  count = 0
  ls_range = [element for element in range(lst[0],lst[-1]+1)]
  for number in ls_range:
    if number not in lst:
      count+=1
  return count

