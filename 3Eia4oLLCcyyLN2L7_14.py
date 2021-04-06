
def remove_repeats(s):
  return "".join(s[i] for i in range(len(s)) if s[i-1] != s[i] or i == 0)

