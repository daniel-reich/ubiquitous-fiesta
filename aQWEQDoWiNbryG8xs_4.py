
def n_tables_plus_one(num):
  lst = []
  for i in range(1,11):
    lst.append((num*i)+1)
  final_str = ','.join([str(lst) for lst in lst]) 
  return final_str

