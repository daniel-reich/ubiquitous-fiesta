
def is_anti_list(lst1, lst2):
  return len(set(lst1+lst2))==2 and all([lst1[i]!=lst2[i] for i in range(len(lst1))])

