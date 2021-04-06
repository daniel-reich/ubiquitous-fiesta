
def shared_digits(lst):
  return all([True if (len(set(str(lst[i])) & set(str(lst[i+1])))) >=1 else False for i in range(len(lst)-1)])

