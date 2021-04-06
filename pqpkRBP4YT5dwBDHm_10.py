
def show_the_love(lst):
  new_lst = []
  lowest = sorted(lst).pop(0)
  new_low = lowest
  indx_low = lst.index(lowest)
  
  for num in lst:
    if num != lowest:
      new_low += num * 0.25
      new_lst.append(num * 0.75)
    else:
      new_lst.append(lowest)
  
  new_lst[indx_low] = new_low
  
  return new_lst

