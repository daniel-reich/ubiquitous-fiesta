
def switch_gravity_on(lst):
  for row in range(len(lst)):
    for col in range(len(lst[0])):
      if lst[row][col] == '#':
        for r in range(len(lst)-1,row,-1):
          if lst[r][col] == '-':
            lst[r][col] = '#'
            lst[row][col] = '-'
            break
  return lst

