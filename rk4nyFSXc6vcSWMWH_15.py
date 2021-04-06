
def shared_digits(lst):
  return all([len(set(str(lst[i]))&set(str(lst[i+1])))>0 for i in range(len(lst)-1)])

