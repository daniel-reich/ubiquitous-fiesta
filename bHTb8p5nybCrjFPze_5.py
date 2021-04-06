
def inclusive_list(start_num, end_num):
  lst = []
  if start_num > end_num:
    return [start_num]
  else: 
    for i in range(start_num, end_num + 1):
      lst.append(i)
  return lst

