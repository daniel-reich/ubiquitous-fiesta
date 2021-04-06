
def grayscale(lst):
  for row in lst:
    for i in range(len(row)):
      for j in range(len(row[i])):
        if row[i][j] < 0:
          row[i][j] = 0
        elif row[i][j] > 255:
          row[i][j] = 255
      g = round(sum(row[i])/3)
      row[i] = [g]*3
  return lst

