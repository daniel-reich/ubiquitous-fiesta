
def moving_partition(lst):
  move = []
  for i in range(0, len(lst)):
    f = lst[:i]
    l = lst[i:]
    move.append([f,l])
  return move[1:]

