
def remove_repeats(s):
  ret = [s[0]]
  for i in s[1:]:
    if not i == ret[-1]:
      ret.append(i)
  return ''.join(ret)

