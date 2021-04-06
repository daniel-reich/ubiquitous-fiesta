
def remove_repeats(s):
  lst = []
  for i in range(len(s)-1):
    if s[i+1] != s[i]: lst.append(s[i])
  if s[-1] != lst[-1]: lst.append(s[-1])
  return "".join(lst)

