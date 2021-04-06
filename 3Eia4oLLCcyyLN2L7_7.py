
def remove_repeats(s):
  return ''.join(s[i] for i in range(len(s)) if i==0 or s[i-1]!=s[i])

