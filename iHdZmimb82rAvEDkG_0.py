
def bitwise_index(lst):
  res = max((n for n in lst if n & 1 == 0), default=None)
  if res == None:
    return 'No even integer found!'
  i = lst.index(res)
  return {"@{} index {}".format(('even','odd')[i & 1], i): res}

