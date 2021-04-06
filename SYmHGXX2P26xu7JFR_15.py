
def number_groups(group1, group2, group3):
  return sorted(list(set([i for i in group1 if i in group2 or i in group3 ]+[j for j in group2 if j in group3])))

