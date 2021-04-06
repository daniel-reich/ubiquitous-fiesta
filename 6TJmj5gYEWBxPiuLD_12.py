
def seating_students(lst):
  seats = [[i for i in range(1,lst[0]+1) if i%2==0],[i for i in range(1,lst[0]+1) if i%2]]
  lst = lst[1:]
  for i in range(len(seats[0])):
    if seats[0][i] in lst:
      seats[0][i] = '#'
    if seats[1][i] in lst:
      seats[1][i] = '#'
  ret = []
  for x in range(len(seats)):
    for y in range(len(seats[x])):
      if seats[x][y]!='#':
        if x==0 and seats[x+1][y]!='#' and sorted([seats[x][y],seats[x+1][y]]) not in ret:
          ret.append(sorted([seats[x][y],seats[x+1][y]]))
        if x>0 and seats[x-1][y]!='#' and sorted([seats[x][y],seats[x-1][y]]) not in ret:
          ret.append(sorted([seats[x][y],seats[x-1][y]]))
        if y>0 and seats[x][y-1]!='#' and sorted([seats[x][y],seats[x][y-1]]) not in ret:
          ret.append(sorted([seats[x][y],seats[x][y-1]]))
        if y<len(seats[x])-1 and seats[x][y+1]!='#' and sorted([seats[x][y],seats[x][y+1]]) not in ret:
          ret.append(sorted([seats[x][y],seats[x][y+1]]))
  return len(ret)

