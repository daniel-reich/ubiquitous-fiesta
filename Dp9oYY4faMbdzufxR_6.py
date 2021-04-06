
def left_slide(row):
  row2 = []
  for i in row:
    if i != 0:
      row2.append(i)
  for i in range(1, len(row2)):
    if row2[i] == row2[i - 1]:
      row2[i - 1] *= 2
      row2[i] = 0
  row_final = []
  for i in row2:
    if i != 0:
      row_final.append(i)
  while len(row_final) != len(row):
    row_final.append(0)
  return row_final

