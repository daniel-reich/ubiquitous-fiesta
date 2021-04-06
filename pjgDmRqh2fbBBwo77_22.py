
def has_syncopation(s):
  return any((i+1)%2==0 for i in range(len(s)) if s[i]=="#")

