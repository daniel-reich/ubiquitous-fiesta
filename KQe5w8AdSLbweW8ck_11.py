
def char_at_pos(r, s):
  lst = []
  index_begin = 0
  if s.lower() == "even":
    index_begin = 1 
  for i in range(index_begin, len(r), 2):
    lst.append(r[i])
  if type(r) == list:
    return lst
  else:
    return ''.join(lst)

