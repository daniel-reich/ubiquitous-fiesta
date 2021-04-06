
daily_streak = lambda t: max(x.count('True')
  for x in ''.join(map(str, t)).split('False'))

