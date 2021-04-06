
def farey(n):
  lst = [[0,"0/1"], [1, "1/1"]]
  for i in range(2, n+1):
    for j in range(1, i):
      if not  j/i in [x[0] for x in lst]:
        lst.append([j/i, "{}/{}".format(j,i)])
  lst.sort()
  return [x[1] for x in lst]

