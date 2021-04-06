
def possible_path(lst):
  if lst[0]=='H':return all([lst[i]=='H' for i in range(0,len(lst),2)])
  return all([lst[i]=='H' for i in range(1,len(lst),2)])

