
def number_groups(group1, group2, group3):
  sg1 = list(set(group1))
  sg2 = list(set(group2))
  sg3 = list(set(group3))
  
  return sorted(set([i for i in sg1 if i in sg2 or i in sg3 ] + [i for i in sg2 if i in sg3]))

