
def grouping(w):
  di = {}
  result = [sum([1 for j in i if j.isupper()]) for i in w]
  result.sort()
  for i in result:
    di[i] = [x for x in w if sum([1 for j in x if j.isupper()]) == i ]
  for i in di:
    temp = [x.lower() for x in di[i]]
    temp.sort()
    for x in range(len(temp)):
      for y in di[i]:
        if y.lower() == temp[x]:
          temp[x] = y
    di[i] = [x for x in temp]
  return di

