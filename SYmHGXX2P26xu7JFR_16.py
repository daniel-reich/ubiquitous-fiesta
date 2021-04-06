
def number_groups(group1, group2, group3):
  output = []
  for i in group1:
    if i in group2 or i in group3:
      output.append(i)
  for i in group2:
    if i in group3:
      output.append(i)
  return sorted(list(set(output)))

