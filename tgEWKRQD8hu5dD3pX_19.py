
def mood_today(*args):
  print(args)
  return 'Today, I am feeling {}'.format(args[0]) if args else "Today, I am feeling neutral"

