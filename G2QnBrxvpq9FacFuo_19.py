
def possible_path(lst):
  return all([lst[i]=='H' for i in range(0,len(lst),2)]) or all([lst[i]!='H' for i in range(0,len(lst),2)])

