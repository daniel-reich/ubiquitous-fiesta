
def is_ladder_safe(ladder):
  index, spacing, counter, new_array = 0, [], 0, []
  for i in ladder:
    if len(i) < 5:
      return False
    x = list(i)
    hashes = 0
    for i in x:
      if i == "#":
        hashes +=1
    spacing.append(hashes)
  for i in spacing:
    if i != spacing[0] and i != spacing[1]:
      return False
    if i == spacing[0] and index != 0:
      counter += 1
    if i == spacing[1] and index != 1:
      new_array.append(counter)
      counter = 0
    index +=1
  for i in new_array:
    if i != new_array[0] or i > 2:
      return False
  return True

