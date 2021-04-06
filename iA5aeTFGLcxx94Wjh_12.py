
def delete_occurrences(lst, num):
  i = 0
  result = []
  while i < len(lst):
    if lst[:i].count(lst[i]) < num:
      result.append(lst[i])
    i += 1
  return(result)

