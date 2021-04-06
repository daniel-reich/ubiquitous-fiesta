
def deadly_virus(persons, n):
  if n == 0:
    return persons
  valid = lambda i,j: min(i,j) >= 0 and i < len(persons) and j < len(persons[0])
  def infected(i,j):
    lst = [(a+i,b+j) for a,b in zip([-1,0,0,1],[0,-1,1,0]) if valid(a+i,b+j)]
    return any(persons[x[0]][x[1]] == "V" for x in lst)
  for k in range(0,n):
    if all((all(c == "V" for c in r) for r in persons)):
      return persons
    persons = [["V" if persons[i][j] == "V" or infected(i,j) else "P" for j in range(0,len(persons[0]))] for i in range(0,len(persons))]
  return persons

