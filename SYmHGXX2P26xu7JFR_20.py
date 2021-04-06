
def number_groups(group1, group2, group3):
  lst = []
  for num in range(11):
    if (num in group1 and num in group2) or (num in group1 and num in group3) or (num in group2 and num in group3):
      lst.append(num)
  return lst

