
def shared_digits(lst):
  return all(len(set(str(lst[x])).intersection(set(str(lst[x + 1])))) >= 1 for x in range(0,len(lst) - 1))

