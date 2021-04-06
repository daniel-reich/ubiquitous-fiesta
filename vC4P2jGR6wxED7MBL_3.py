
def larger_than_right(lst):
  largest_lst = []
  for num in range(len(lst)):
    if num == len(lst) - 1:
      largest_lst.append(lst[num])
      break
    if lst[num] > max(lst[num + 1:]):
      largest_lst.append(lst[num])
  return largest_lst

