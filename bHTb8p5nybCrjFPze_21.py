
def inclusive_list(start_num, end_num):
  b = []
  for a in range(start_num, end_num + 1):
    b.append(a)
  if start_num > end_num:
    b.append(start_num)
  return b

