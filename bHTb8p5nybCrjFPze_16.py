
def inclusive_list(start_num, end_num):
  list_ret = []
  if start_num > end_num:
    list_ret = [start_num]
  for i in range(start_num, end_num + 1):
    list_ret.append(i)
  return list_ret

