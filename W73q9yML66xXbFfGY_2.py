
def coloured_triangle(row):
  while len(row) > 1:
    new = ""
    for i in range(len(row) - 1):
      if row[i] == row[i+1]:
        new += row[i]
      else:
        for j in "RBG":
          if j not in row[i:i+2]:
            new += j
    row = new
  return row

