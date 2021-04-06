
def missing_letter(lst):
  lst = list(map(ord,lst))
  return chr(sum(range(lst[0],lst[-1]+1)) - sum(lst))

