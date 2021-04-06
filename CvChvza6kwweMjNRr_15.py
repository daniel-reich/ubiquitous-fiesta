
def split_code(item):
  c=''
  n=''
  for i in item:
    if i.isdigit()==True:
      n+=i
    else:
      c+=i
  return [c, int(n)]

