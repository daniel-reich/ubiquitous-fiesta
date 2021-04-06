
def remove_repeats(s):
  s_final = ''
  for i in range(len(s)-1):
    if s[i] == s[i+1]:
      continue
    else:
      s_final += s[i]
  return s_final+s[-1]

