
def deadly_virus(people, n):
  len_x = len(people); len_y = len(people[0])
  for hour in range(n):
    infected = set()
    for i in range(len_x):
      for j in range(len_y):
        if people[i][j] == 'V':
          if i > 0:
            infected.add((i - 1, j))
          if i < (len_x - 1):
            infected.add((i + 1, j))
          if j > 0:
            infected.add((i, j - 1))
          if j < (len_y - 1):
            infected.add((i, j + 1))
    for i, j in infected:
      people[i][j] = 'V'
  return people

