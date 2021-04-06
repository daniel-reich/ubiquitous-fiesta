
def invert_list(lst):
  inverted_lst = []
  for i in lst:
    if i < 0:
      inverted_lst.append(abs(i))
    else:
      inverted_lst.append(-i)
      
  return inverted_lst

