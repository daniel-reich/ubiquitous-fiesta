
def inclusive_list(start_num, end_num):
  if start_num < end_num:
    return list(range(start_num, end_num + 1))
  return [start_num]

