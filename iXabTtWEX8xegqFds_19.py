
def alternate_sort(lst):
  num = sorted(list(filter(lambda x: type(x) == int, lst)))
  char = sorted(list(filter(lambda x: str(x).isalpha(), lst)))
  for i in range(len(lst)):
    if i % 2 == 0:
      lst[i] = num[i // 2]
    else:
      lst[i] = char[i//2]
  return lst

