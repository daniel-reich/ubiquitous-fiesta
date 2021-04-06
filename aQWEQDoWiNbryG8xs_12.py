
def n_tables_plus_one(num):
  return ",".join(map(str, [item for item in range(num + 1, num * 10 + 2, num)]))

