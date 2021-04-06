
def remove_zero(row):
  ans = []
  for i in row:
    if i:
      ans.append(i)
  return ans
def left_slide(row):
  merging = remove_zero(row.copy())
  for i in range(len(merging)-1):
    if merging[i] == merging[i+1]:
      merging[i], merging[i+1] = merging[i]*2, 0
  merged = remove_zero(merging)
  merged = merged + [0]*(len(row)-len(merged))
  return merged

