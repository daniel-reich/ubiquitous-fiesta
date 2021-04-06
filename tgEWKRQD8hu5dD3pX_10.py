
def mood_today(*mood):
  if len(mood) != 0:
    return "Today, I am feeling "+ mood[0]
  else:
    return "Today, I am feeling neutral"

