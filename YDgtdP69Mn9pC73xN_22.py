
def num_grid(lst):
  for i in range(0, len(lst)):
    for j in range(0, len(lst[i])):
      if lst[i][j] == "-":
        lst[i][j] = 0  
​
  for i in range(0, len(lst)):
    for j in range(0, len(lst[i])):
      if lst[i][j] == "#":
        if j+1 > len(lst[i]) - 1:
          pass
        elif type(lst[i][j+1]) == int:
          lst[i][j+1] = lst[i][j+1] + 1
        elif type(lst[i][j+1]) != int:
          lst[i][j+1] = lst[i][j+1]
​
        if j-1 < 0:
          pass
        elif type(lst[i][j-1]) == int:
          lst[i][j-1] = lst[i][j-1] + 1
        elif type(lst[i][j-1]) != int:
          lst[i][j-1] = lst[i][j-1]
​
        if i-1 < 0:
          pass
        elif type(lst[i-1][j]) == int:
          lst[i-1][j] = lst[i-1][j] + 1
        elif type(lst[i-1][j]) != int:
          lst[i-1][j] = lst[i-1][j]
        
        if i+1 > len(lst) - 1:
          pass
        elif type(lst[i+1][j]) == int:
          lst[i+1][j] = lst[i+1][j] + 1
        elif type(lst[i-1][j]) != int:
          lst[i+1][j] = lst[i+1][j]
        
        if j-1 < 0 or i+1 > len(lst) - 1:
          pass
        elif type(lst[i+1][j-1]) == int:
          lst[i+1][j-1] = lst[i+1][j-1] + 1
        elif type(lst[i-1][j]) != int:
          lst[i+1][j-1] = lst[i+1][j-1]
​
        if j+1 > len(lst[i]) - 1 or i+1 > len(lst) - 1:
          pass
        elif type(lst[i+1][j+1]) == int:
          lst[i+1][j+1] = lst[i+1][j+1] + 1
        elif type(lst[i-1][j]) != int:
          lst[i+1][j+1] = lst[i+1][j+1]
        
        if j-1 < 0 or i-1 < 0:
          pass
        elif type(lst[i-1][j-1]) == int:
          lst[i-1][j-1] = lst[i-1][j-1] + 1
        elif type(lst[i-1][j]) != int:
          lst[i-1][j-1] = lst[i-1][j-1]
​
        if j+1 > len(lst[i]) - 1 or i-1 < 0:
          pass
        elif type(lst[i-1][j+1]) == int:
          lst[i-1][j+1] = lst[i-1][j+1] + 1
        elif type(lst[i-1][j]) != int:
          lst[i-1][j+1] = lst[i-1][j+1]
  for i in range(0, len(lst)):
    for j in range(0, len(lst[i])):
      lst[i][j] = str(lst[i][j])
  return lst

