
def move_to_end(lst, el):
  count, final = 0, []
  for char in lst:
    if char == el:
      count += 1
    else:
      final.append(char)
  for _ in range(count): final.append(el)
  return final

