
def min_removals(txt1, txt2):
  count1 = count2 = 0
  for x in txt1:
    if x not in txt2:
      count1 += 1
  for x in txt2:
    if x not in txt1:
      count2 += 1
  count = count1 + count2
  return count

