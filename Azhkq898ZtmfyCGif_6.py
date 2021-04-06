
def numbers_to_ranges(lst):
  range_list = []
  start = 0
  for i in range(len(lst)):
    if i+1 < len(lst) and lst[i+1] == lst[i] + 1:
      continue
    else:
      range_list.append(lst[start:i+1])
      start = i + 1
  return [str(max(i)) if len(i) == 1 else '{}-{}'.format(min(i), max(i)) for i in range_list]

