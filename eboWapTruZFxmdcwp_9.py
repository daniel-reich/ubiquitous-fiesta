
def is_positive_dominant(lst):
  
  s = list(set(lst))
  
  pos_count = 0
  neg_count = 0
  
  for item in s:
    if item >0:
      pos_count += 1
    elif item == 0:
      continue
    else:
      neg_count += 1
  
  return pos_count > neg_count

