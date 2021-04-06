
def bird_code(lst):
​
  tran_lst = []
  for name in lst:
    name = name.replace(r'\\',' ')
    name = name.replace('-', ' ')
    name = name.split()
​
    if len(name) == 1:
      tran_lst.append(name[0][:4].upper())
    elif len(name) == 2:
      tran_lst.append(name[0][:2].upper()+name[1][:2].upper())
​
    elif len(name) == 3:
      tran_lst.append(name[0][0].upper()+name[1][0].upper()+name[2][:2].upper())
    elif len(name) == 4:
      tran_lst.append(name[0][0].upper()+name[1][0].upper()+name[2][0].upper()+name[3][0].upper())
  return tran_lst

