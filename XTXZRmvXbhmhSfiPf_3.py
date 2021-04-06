
def single_number(r):
  s = sorted(r)
  for i in range(0, len(s), 3):
    if i == len(s)-1 or s[i] < s[i+1]: return s[i]

