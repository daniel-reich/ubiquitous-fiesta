
def list_to_string(lst):
  a=""
  for i in lst:
    if type(i)==str:
      a+=i
    elif type(i)!=str:
      i=str(i)
      a+=i
  return a

