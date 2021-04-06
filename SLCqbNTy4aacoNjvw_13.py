
def remove_dups(lst):
  seen = []
  for i in range(0, len(lst)):
    if lst[i] not in seen:
      seen.append(lst[i])
  return seen

