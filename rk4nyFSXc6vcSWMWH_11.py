
def shared_digits(lst):
  return len([x for x in range(len(lst)-1)  if len(set(str(lst[x]))&set(str(lst[x+1])))!=0])==len(lst)-1

