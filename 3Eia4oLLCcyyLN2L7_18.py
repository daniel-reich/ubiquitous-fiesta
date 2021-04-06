
def remove_repeats(s):
  return "".join([s[i] for i in range(0,len(s)-1) if s[i]!=s[i+1]])+s[-1]

