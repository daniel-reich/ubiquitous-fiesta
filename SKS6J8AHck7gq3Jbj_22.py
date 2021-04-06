
def tidy_books(lst):
  import re
  lst1 = []
  for i in lst:
    i = re.findall(r'[^-]+', i[0])
    i[0] = i[0].strip()
    i[1] = i[1].strip()
    lst1.append(i)
  return lst1

