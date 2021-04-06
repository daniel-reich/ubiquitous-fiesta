
def daily_streak(lst):
  if not any([i for i in lst]):
    return 0
  lst = ''.join(['T' if i else ' ' for i in lst]).split()
  return max([len(i) for i in lst])

