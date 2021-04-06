
def number_groups(group1, group2, group3):
  a = set(group1)
  b = set(group2)
  c = set(group3)
  return sorted([i for i in (a&b | a&c | b&c)])

