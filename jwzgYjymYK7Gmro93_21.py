
def get_indices(lst, el):
  number = 0
  record = []
  if el not in lst:
    return []
  while number < len(lst):
    if lst[number] == el:
      record.append(number)
      number += 1
    else:
      number += 1
  return record

