
def daily_streak(lst):
  a = ''.join([str(i) for i in lst]).split('False')
  return max(i.count('True') for i in a)

