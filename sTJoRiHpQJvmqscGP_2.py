
def daily_streak(lst):
  c=0
  for i in range(len(lst)):
    if "True"*i in "".join((map(str,lst))):c=i
  return c

