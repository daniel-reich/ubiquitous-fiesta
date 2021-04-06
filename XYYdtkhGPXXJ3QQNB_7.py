
def num_in_str(lst):
  results = []
  for item in lst:
    for i in item:
      if i.isnumeric():
        results.append(item)
        break
  return results

