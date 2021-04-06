
def rep_set(n):
  return list(map(lambda x: rep_set(x), range(n)))

