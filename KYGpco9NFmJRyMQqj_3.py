
def min_removals(txt1, txt2):
  count = 0
  for i in range(max(len(txt1), len(txt2))):
    if i < len(txt1):
      count += txt1[i] not in txt2
    if i < len(txt2):
      count += txt2[i] not in txt1
  return count

