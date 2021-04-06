
def asc_des_none(lst, s):
  if s == None:
    return lst 
  return sorted(lst)[::-1] if s == "Des" else sorted(lst)

