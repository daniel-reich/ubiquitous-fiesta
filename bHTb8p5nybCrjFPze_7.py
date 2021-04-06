
def inclusive_list(start_num, end_num):
  return list(i for i in range(start_num, end_num + 1)) if start_num < end_num else [start_num]

