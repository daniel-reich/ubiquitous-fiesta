
def n_tables_plus_one(num):
  out = ""
  for i in range(1, 11):
    out += str(num * i + 1)
    if(i != 10):
      out += ","
  return out

