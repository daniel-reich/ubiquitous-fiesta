
def inclusive_list(start_num, end_num):
  lst = [start_num]
  if start_num >= end_num: return lst
  else:
    for i in range(1, (end_num - start_num)+1):
      lst.append(start_num + i)
  return lst

