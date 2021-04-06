
def inclusive_list(start_num, end_num):
  if start_num >= end_num:
    return [start_num]
  return [start_num] + inclusive_list(start_num+1, end_num)

