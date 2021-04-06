
def dance(lst, parameter):
  w = [i[0] for i in lst]
  m = [i[1] for i in lst]
  if parameter == "men":
    ret = list(zip(w,m[::-1]))
  else:
    ret = list(zip(w[::-1],m))
  return [list(i) for i in ret]

