
def wiggle_string(s):
  r = [' '*l + s for l in range(len(s)+1)]
  return r+r[-2::-1]

