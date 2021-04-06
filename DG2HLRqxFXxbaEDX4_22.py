
def return_only_integer(l):
  o = []
  for i in l:
    if 'int' in str(type(i)):
      o.append(i)
  return o

