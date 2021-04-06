
def look_and_say(n):
  n_s = str(n)
  if len(n_s) % 2 != 0:
    return "invalid"
  else:
    var = ""
    i = 0
    while i < len(n_s):
      j = 0
      while j < int(n_s[i]):
        var = var + n_s[i+1]
        j = j + 1
      i = i + 2
  return int(var)

