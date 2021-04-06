
def majority_vote(lst):
  n = len(lst)/2
  check = {}
  count = 0
  final = ""
  for x in lst:
    if x not in check:
      check[x] = 1
    else:
      check[x] += 1
  for key, value in check.items():
    if value >= n:
      count += 1
      final = key
  if count > 1 or count == 0:
    return None
  return final

