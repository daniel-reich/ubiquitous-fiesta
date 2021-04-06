
def wiggle_string(s):
  return [" "*i+s for i in range(len(s)+1)] + [" "*i+s for i in range(len(s)+1)][::-1][1:]

