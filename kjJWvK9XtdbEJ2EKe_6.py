
def sort_array(lst):
  while True:
    c = 0
    for i in range(len(lst)-1):
      if lst[i] > lst[i+1]:
        lst[i],lst[i+1] = lst[i+1], lst[i]
        c += 1
    if c == 0:
      break
  return lst

