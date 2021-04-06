
def join_digits(n):
  lst = []
  chars = []
  for i in range(n):
    lst.append(str(i + 1))
  for i in range(len(lst)):
    for j in range(len(lst[i])):
      chars.append(lst[i][j])
  return "-".join(chars)

