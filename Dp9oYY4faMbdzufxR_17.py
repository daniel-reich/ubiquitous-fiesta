
def left_slide(row):
  merged = [False] * len(row)
  for i in range(1, len(row)):
    while i >= 1:
      if row[i - 1] == 0:  # Move
        row[i - 1] = row[i]
        merged[i - 1] = merged[i]
      elif row[i - 1] == row[i] and not merged[i - 1] and not merged[i]:  # Merge
        row[i - 1] = row[i] * 2
        merged[i - 1] = True
      else:
        break
      # We moved or merged:
      row[i] = 0
      merged[i] = False
      i = i - 1  # Keep sliding to the left.
  return row

