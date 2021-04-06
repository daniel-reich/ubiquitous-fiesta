
def pos_neg_sort(lst):
  pos_list = sorted([x for x in lst if x > 0])
  
  pos_pointer = 0
  for i in range(len(lst)):
    if lst[i] > 0:
      lst[i] = pos_list[pos_pointer]
      pos_pointer += 1
  return lst

