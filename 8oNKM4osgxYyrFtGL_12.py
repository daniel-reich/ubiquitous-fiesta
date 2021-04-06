
def multiply(l):
  big_list = []
  for i in l:
    i_list = []
    for j in range(0,len(l)):
      i_list.append(i)
    big_list.append(i_list)
  return big_list

