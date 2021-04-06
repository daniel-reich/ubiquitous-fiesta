
def daily_streak(lst):
  return max(str(lst)[1:-1].split('False'),key=lambda x:len(x)).count('True')

