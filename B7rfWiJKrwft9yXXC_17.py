
def sort_decending(num):
  ls = []
  x = str(num)
  for char in x:
    ls.append(char)
  return int("".join(sorted(ls, reverse=True)))

