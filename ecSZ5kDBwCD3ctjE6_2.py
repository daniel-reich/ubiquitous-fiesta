
def find_smallest_num(lst):
  mn=lst[0]
  for i in range(len(lst)):
    if lst[i]<mn: mn=lst[i]
  return mn

