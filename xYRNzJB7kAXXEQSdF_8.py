
def wiggle_string(s):
  return [" "*i+s for i in range(len(s))]+[" "*len(s)+s]+[" "*i+s for i in range(len(s))][::-1]

