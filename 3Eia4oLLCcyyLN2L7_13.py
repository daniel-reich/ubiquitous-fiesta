
def remove_repeats(s):
  result = ""
  for i in range(len(s) - 1):
    if s[i] == s[i + 1]:
      continue
    else:
      result += s[i]
  return result + s[-1]

