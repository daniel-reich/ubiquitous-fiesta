
def num_grid(lst):
  x = [
      [0,0,0,0,0],
      [0,0,0,0,0],
      [0,0,0,0,0],
      [0,0,0,0,0],
      [0,0,0,0,0],
  ]
  a = []
  b = []
  for i in range(len(lst)):
    for j in range(len(lst[i])):
      if lst[i][j] == '#':
        x[i][j] = -100
        try:
          index1 = i
          index2 = j-1
          if index1 >=0 and index2 >=0:
            x[i][j-1] += 1
        except:
          pass
        try:
          index1 = i
          index2 = j+1
          if index1 >= 0 and index2 >=0:
            x[i][j+1] += 1
        except:
          pass
        try:
          index1 = i-1
          index2 = j
          if index1 >=0 and index2 >=0:
            x[i-1][j] += 1
        except:
          pass
        try:
          index1 = i+1
          index2 = j
          if index1 >=0and index2>=0:
            x[i+1][j] += 1
        except:
          pass
        try:
          index1 = i-1
          index2 = j-1
          if index1 >=0and index2>=0:
            x[i-1][j-1] +=1
        except:
          pass
        try:
          index1 = i-1
          index2 = j+1
          if index1 >=0and index2>=0:
            x[i-1][j+1] += 1
        except:
          pass
        try:
          index1 = i+1
          index2 = j-1
          if index1 >=0and index2>=0:
            x[i+1][j-1] += 1
        except:
          pass
        try:
          index1 = i+1
          index2 = j+1
          if index1 >=0and index2>=0:
            x[i+1][j+1] += 1
        except:
          pass
          
  for k in x:
    a = []
    for l in k:
      if l<0:
        a.append('#')
      else:
        a.append(str(l))
    b.append(a)
  return b

