
def asc_des_none(lst, s):
  if s == 'Asc':
    lst.sort()
  if s == 'Des':
    lst.sort(reverse=True)
  return lst

