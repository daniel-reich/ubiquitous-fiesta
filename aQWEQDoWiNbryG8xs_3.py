
def n_tables_plus_one(num):
  return ",".join([str(x+num*(y+1)) for y,x in enumerate([1 for x in list(range(1,11))])])

