
def inclusive_list(start_num, end_num):
  if end_num <= start_num:
    return [start_num]
  else:
    return [i for i in range(start_num, end_num+1)]

