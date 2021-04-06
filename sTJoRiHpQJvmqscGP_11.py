
def daily_streak(lst):
  s=str(lst).split('False')
  A=[x.count('True') for x in s]
  return max(A)

