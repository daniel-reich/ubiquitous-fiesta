
def find_missing(lst):
  if lst == None or lst == []:
    return False
  sorted_lst = sorted(lst, key = lambda x: len(x))
  for i in range(1,len(sorted_lst)):
    if sorted_lst[i-1] == []:
      return False
    diff = len(sorted_lst[i]) - len(sorted_lst[i-1])
    if diff != 1:
      return len(sorted_lst[i-1]) + 1

