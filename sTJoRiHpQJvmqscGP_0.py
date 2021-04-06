
def daily_streak(lst):
  return len(max(''.join(map(str,lst)).split('False'), key = len))//4

