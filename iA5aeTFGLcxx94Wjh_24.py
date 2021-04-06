
def delete_occurrences(lst, num):
  out = []
  for elem in lst:
    if out.count(elem) < num:
      out.append(elem)
  return out

