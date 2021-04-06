
def sum_of_holes(N):
  one = "4690"
  two = "8"
  holes = 0
  for i in range(1, N+1):
    i = str(i)
    for j in i:
      if j in one:
        holes+=1
      elif j in two:
        holes +=2
  return holes

