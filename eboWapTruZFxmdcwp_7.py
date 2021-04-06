
def is_positive_dominant(lst):
  pos = 0
  pos_nums = []
  neg = 0
  neg_nums = []
  for i in lst:
    if i > 0 and i not in pos_nums:
      pos += 1
      pos_nums.append(i)
    elif i < 0 and i not in neg_nums:
      neg += 1
      neg_nums.append(i)
  return pos > neg

