
def mood_today(*mood):
  return "Today, I am feeling {}".format(mood[0] if mood else 'neutral')

