
def combine(lst):
  keys = sorted(set([x[0] for x in lst]))
  positions = len(set([x[1] for x in lst]))
  result = {key: [x for x in range(positions)] for key in keys}
  for i in range(len(lst)):
    result[lst[i][0]][lst[i][1]] = lst[i][2]
  return (result)

