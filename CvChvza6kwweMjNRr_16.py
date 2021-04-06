
def split_code(item):
  strhold = ''
  inthold = ''
  for x in range(len(item)):
    if item[x].isalpha():
      strhold = strhold + item[x]
    else:
      inthold = inthold + item[x]
  lst = [strhold,int(inthold)]
  return lst

