
def move_to_end(lst, el):
  result = []
  for num in lst:
    if num != el:
      result.append(num)
  for num in lst:
    if num == el:
      result.append(num)
  return result

