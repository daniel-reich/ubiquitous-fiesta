
def char_at_pos(r, s):
  lst = []
  if s == "even":
    for i in range(1, len(r),2):
      lst.append(r[i])
  else:
    for i in range(0, len(r),2):
      lst.append(r[i])
  if type(r) == str:
    return "".join(lst)
  return lst

