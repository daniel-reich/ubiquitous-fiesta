
def deadly_virus(persons, n):
  if n == 0:
    return persons
​
  h, w = len(persons), len(persons[0])
  return deadly_virus(
    [[
      "V" if any(persons[d][e] == "V" for d, e in [[i + y, j + x] for y, x in [[1, 0], [0, 1], [-1, 0], [0, -1]] if 0 <= i + y < h and 0 <= j + x < w]) else b
    for j, b in enumerate(a)] for i, a in enumerate(persons)]
  , n - 1)

