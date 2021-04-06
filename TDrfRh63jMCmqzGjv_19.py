
def is_anti_list(lst1, lst2):
  return len([i for i in range(len(lst1)) if lst1[i]==lst2[i]])==0 and len(set(lst1+lst2)) == 2

