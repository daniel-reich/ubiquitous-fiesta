
def last_name_lensort(names):
  lst = []
  for i in names:
    if len(lst) == 0:
      lst.append(i)
    else:
      lst = sort(i, lst)
  return lst
​
def sort(name, lst):
  lastname = get_lastname(name)
  for i in range(len(lst)):
    compare_lastname = get_lastname(lst[i])
    if len(lastname) < len(compare_lastname):
      lst.insert(i, name)
      break
    elif len(lastname) == len(compare_lastname):
      if ord(lastname[0]) <  ord(compare_lastname[0]):
        lst.insert(i, name)
      else:
        lst.insert(i+1, name)
      break
    elif i == len(lst)-1:
      lst.insert(i, name)
      break
  return lst
      
def get_lastname(name):
  index_space = name.find(" ")
  lastName = name[index_space+1:]
  return lastName

