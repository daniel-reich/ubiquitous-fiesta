
def inclusive_list(start_num, end_num):
  a = []
  if end_num<start_num:
    return [start_num]
  for i in range(start_num, end_num + 1):
    a.append(i)
  return a

