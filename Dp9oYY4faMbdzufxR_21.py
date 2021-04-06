
def left_slide(row):
  i = 0
  while True:
    if row[i::].count(0) == len(row[i::]):
      return row
    elif row[i+1::].count(0) == len(row[i+1::]):
      return row
    elif row[i] == 0:
      row.pop(i)
      row.append(0)
    elif row[i+1] == 0:
      row.pop(i+1)
      row.append(0)
    else:
      if row[i] == row[i+1]:
        row[i] *= 2
        row.pop(i+1)
        row.append(0)
      i += 1

