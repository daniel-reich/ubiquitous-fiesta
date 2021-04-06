
def wiggle_string(s):
  lst = [' ' * i + s for i in range(len(s)+1)]
  return lst[:-1] + lst[::-1]

