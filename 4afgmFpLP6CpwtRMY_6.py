
def sudoku_validator(x):
  bag = lambda x: sorted(x) == [1,2,3,4,5,6,7,8,9]
  rows = [bag(row) for row in x]
  cols = [bag([row[y] for row in x]) for y in range(9)]
  sections = []
  combos = [(0,3),(3,6),(6,9)]
  for i in combos:
    for j in combos:
      sections.append(bag([z for y in [[row[col] for row in x[i[0]:i[1]]]for col in range(j[0],j[1])] for z in y]))
  return all(rows) and all(cols) and all(sections)

