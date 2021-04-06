
def has_syncopation(s):
  return any (i for i in range(len(s)) if i % 2 == 1 and s[i] == "#")

