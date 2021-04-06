
def deadly_virus(persons, n):
  for i in range(n):
    temp = [[x for x in y] for y in persons]
    for x in range(len(temp)):
      for y in range(len(temp[x])):
        if x>0 and persons[x-1][y]=='V':
          temp[x][y]='V'
        if x<len(persons)-1 and persons[x+1][y]=='V':
          temp[x][y]='V'
        if y>0 and persons[x][y-1]=='V':
          temp[x][y]='V'
        if y<len(persons[x])-1 and persons[x][y+1]=='V':
          temp[x][y]='V'
    persons=temp
  return persons

