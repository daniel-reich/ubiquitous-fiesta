
def deadly_virus(persons, n):
  temp = [i[:] for i in persons]
  for h in range(n):
    for i in range(len(temp)):
      for j in range(len(temp[0])):
        if persons[i][j]=='V':
          temp[max(i-1,0)][j] = 'V'
          temp[min(len(temp)-1,i+1)][j] = 'V'
          temp[i][max(j-1,0)] = 'V'
          temp[i][min(len(temp[0])-1,j+1)] = 'V'
    persons = [i[:] for i in temp]
  return persons

