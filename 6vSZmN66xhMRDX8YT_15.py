
def advanced_sort(lst):
  found = []
  final = []
  for item in lst:
    if item not in found:
      count = lst.count(item)
      sub = []
      for _ in range(count):
        sub.append(item)
      final.append(sub)
      found.append(item)
  return final

