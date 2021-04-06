
def number_groups(group1, group2, group3):
  return list(sorted(set([x for x in group1 if x in (group2+group3)]+[x for x in group2 if x in (group1+group3)]+[x for x in group3 if x in (group2+group1)])))

