
def diagonalize(n, d):
  lst = [0] * n
  for i in range(len(lst)):
    lst[i] = [0]*n
  it = 0
  for i in range(len(lst)):
    for x in range(len(lst[0])):
      lst[i][x] = x+it
    it+=1
  if d[0] == 'l':
    lst = lst[::-1]
  if d[1] == 'r':
    lst = [i[::-1] for i in lst]
  for i in lst:
    print(i)
  return lst

