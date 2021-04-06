
def title_to_number(s):
  string = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
  if len(s) == 1:
    return string.index(s) + 1
  return 26 * title_to_number(s[:-1]) + string.index(s[-1]) + 1

