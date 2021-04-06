
def switch_gravity_on(lst):
  boxes = [0]*len(lst[0])
  for i in range(len(lst[0])):
    boxes[i] = len([j for j in range(len(lst)) if lst[j][i]=='#'])
  for i in range(len(lst)):
    for j in range(len(lst[i])):
      if i-boxes[j]<0:
        lst[i][j] = '#'
      else:
        lst[i][j] = '-'
  return lst[::-1]

