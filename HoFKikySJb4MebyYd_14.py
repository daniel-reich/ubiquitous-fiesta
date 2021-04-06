
def get_sum(a):
  return [ [sum(i)-1 if j == 1 else sum(i) for j in i] for i in a ]
​
def transform_matrix(lst):
  col_lst = get_sum(lst)
  zip_lst = list(zip(*lst))
  zip_lst_sum = get_sum(zip_lst)
  row_lst = list(zip(*zip_lst_sum))
  return [ [col_lst[i][j]+ row_lst[i][j] for j in range(len(lst[i])) ] for i in range(len(lst)) ]

