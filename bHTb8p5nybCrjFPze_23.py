
def inclusive_list(start_num, end_num):
  if start_num>end_num:
    return [start_num]
  else:
    return list(range(start_num,end_num+1,1))

