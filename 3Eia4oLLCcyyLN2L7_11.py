
def remove_repeats(s):
  lst = []
  s = list(s)
  lst.append(s[0])
  for i in range(1, len(s)):
    if s[i] != lst[-1]:
      lst.append(s[i])
  return "".join(lst)

