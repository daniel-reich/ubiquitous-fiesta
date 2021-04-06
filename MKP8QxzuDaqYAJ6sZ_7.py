
def is_correct_aliases(names, aliases):
  count = 0
  for i in range(len(names)):
    y = aliases[i].split()
    if y[0].startswith(names[i][0]) and y[1].startswith(names[i][0]):
      count += 1
  if count == len(names):
    return True
  return False

