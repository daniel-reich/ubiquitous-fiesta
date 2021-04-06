
def is_positive_dominant(lst):
  pos = 0
  neg = 0
  stlst = set(lst)
  for i in stlst:
    if i > 0:
      pos += 1
    elif i < 0:
      neg += 1
  return pos > neg

