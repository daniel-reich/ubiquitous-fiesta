
def reorder_digits(lst, direction):
  result = []
  if direction == "asc":
    for i in lst:
      result.append(int("".join(sorted(str(i)))))
  else:
    for i in lst:
      result.append(int("".join(sorted(str(i),reverse=True))))
  return result

