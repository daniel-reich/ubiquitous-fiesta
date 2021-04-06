
def larger_than_right(lst):
  other_lst = []
  other_lst.append(lst[-1])
  for i in range(len(lst)-2, -1, -1):
    if lst[i] > max(other_lst):
      other_lst.insert(0, lst[i])
  return other_lst

