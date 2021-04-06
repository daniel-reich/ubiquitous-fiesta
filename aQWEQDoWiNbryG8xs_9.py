
def n_tables_plus_one(num):
  res = ''
  for i in range(1,11):
    res += str(i*num+1) + ','
  return res [:-1]

