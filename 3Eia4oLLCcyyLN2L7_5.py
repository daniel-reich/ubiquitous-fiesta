
def remove_repeats(s):
  return s[0] + ''.join([s[i] for i in range(1,len(s)) if s[i-1]!=s[i]])

