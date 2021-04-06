
def shared_digits(lst):
  return all(set(str(lst[i-1]))&set(str(lst[i])) for i in range(1, len(lst)))

