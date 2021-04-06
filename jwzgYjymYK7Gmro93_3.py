
def get_indices(lst, el):
  foo = []
  for i in range(len(lst)):
    if el == lst[i]:
      foo.append(i)
  return foo

