
def number_of_repeats(s):
  for i in range(1,len(s)+1):
    k = len(s)//i
    if s == s[:i]*k:
      return k

