
def remove_repeats(s):
  new = ""
  for i in range(len(s)-1):
    if s[i+1] != s[i]:
      new += s[i]
  return new + s[-1]

