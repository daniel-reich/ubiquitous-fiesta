
def block(lst):
  done = set()
  cnt = 0
  for i in range(len(lst)):
    for j in range(len(lst[0])):
      if j in done:
        continue
      if lst[i][j] == 2:
        cnt += len(lst)-i-1
        done.add(j)
  return cnt

