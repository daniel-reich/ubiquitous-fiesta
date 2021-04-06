
def check(f, s, x):
  try:
    if f[x] == s[x]:
      return True
  except:
    return "One's empty"
  else:
    return 'Not the same'

