
def return_only_integer(lst):
  lstint = []
  for s in lst:
    if type(s) == int:
      lstint.append(s)
  return lstint

