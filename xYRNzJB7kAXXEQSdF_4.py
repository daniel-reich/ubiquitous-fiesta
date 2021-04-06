
def wiggle_string(s):
  half = [' '*i + s for i in range(len(s) + 1)]
  return half + half[:-1][::-1]

