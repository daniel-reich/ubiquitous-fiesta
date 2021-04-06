
def loves_me(n):
  solution_string = ''
  for counter in range(n):
    if counter == n - 1:
      if solution_string == '' or 'not' in solution_string[-5:]:
        solution_string += "LOVES ME"
      else:
        solution_string += "LOVES ME NOT"
    elif counter % 2 == 0:
      solution_string += 'Loves me, '
    else:
      solution_string += 'Loves me not, '
​
  return solution_string

