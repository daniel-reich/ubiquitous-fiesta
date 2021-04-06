
def validate_subsets(s,m):
  return set([j for i in s for j in i]).issubset(m)

