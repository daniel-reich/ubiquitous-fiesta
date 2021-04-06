
def is_checkerboard(lst):
  return [x[0] for x in list(zip(lst))] == lst \
  and len(set(tuple(row) for row in lst[0::2]) ) == 1 \
  and len(set(tuple(row) for row in lst[1::2]) ) == 1 \
  and set(lst[0][0::2]) != set(lst[0][1::2]) \
  and set(lst[1][0::2]) != set(lst[1][1::2])

