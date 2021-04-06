
def move_zeros(lst):
  zero_lst = []
  nonzero_lst =[]
  zero_lst.append([x for x in lst if (x == 0 and x is not False)])  
  nonzero_lst.append([x for x in lst if (x != 0 or x is False)])
  lst_sorted = nonzero_lst + zero_lst
  lst_final = [x for l in lst_sorted for x in l] #unpacking the list
​
  print(lst_final)
  return lst_final

