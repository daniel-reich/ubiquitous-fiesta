
def inclusive_list(start_num, end_num):
  return [start_num] if end_num < start_num else list(range(start_num, end_num + 1))

