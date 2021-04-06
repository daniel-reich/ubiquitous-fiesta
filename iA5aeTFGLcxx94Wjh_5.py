
def delete_occurrences(lst, num):
  counter = {item: 0 for item in set(lst)}
  result = []
  for item in lst:
    if counter[item] < num:
      result.append(item)
      counter[item] += 1
  return result

