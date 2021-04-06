
def number_groups(group1, group2, group3):
  one = list(set(group1))
  second = list(set(group2))
  third = list(set(group3))
  x = [one, second, third]
  new_list = []
  for i in x:
    for a in i:
      new_list.append(a)
  print(new_list)
  final = list(set([i for i in new_list if new_list.count(i) > 1]))
  return sorted(final)

