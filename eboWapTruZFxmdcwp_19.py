
def is_positive_dominant(lst):
  pos, neg = 0, 0
  for i in set(lst):
    if i > 0:
     pos += 1
    elif i < 0:
      neg += 1
  return pos > neg

