
def shared_digits(lst):
  lst = [set(str(i)) for i in lst]
  lst = [True if len(lst[i] & lst[i+1]) else False for i in range(len(lst)-1)]
  return all(lst)

