
def deadly_virus(persons, n):
  while n:
    persons = update(spread(infected(persons)))
    n -= 1
  return persons
​
def infected(matrix):
  result = []
  for index, row in enumerate(matrix):
    for i, person in enumerate(row):
      if person == 'V':
        result.append((index, i))
  return result
  
def spread(lst):
  result = []
  for (x, y) in lst:
    new = ((x+1, y), (x-1, y), (x, y+1), (x, y-1))
    for (a, b) in new:
      if a >= 0 and a <= 5 and b >=0 and b <= 5:
        result.append((a, b))
  result.extend(lst)
  return result
  
def update(lst):
  return [
    ['V' if (index, i) in lst else 'P' for i in range(5)]
    for index in range(5)
  ]

