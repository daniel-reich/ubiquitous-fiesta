
def is_positive_dominant(lst):
  pos_num = set()
  pos_count = 0
  neg_num = set()
  neg_count = 0
  for l in lst:
    if l > 0 and l not in pos_num:
      pos_num.add(l)
      pos_count+=1
    if l < 0 and l not in neg_num:
      neg_num.add(l)
      neg_count+=1
  return pos_count > neg_count

