
def number_groups(group1, group2, group3):
  return sorted(list(set([num for num in group1 if (group2.count(num)>0 or group3.count(num)>0)]+[num for num in group2 if group3.count(num)>0])))

