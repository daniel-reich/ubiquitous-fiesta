
def number_of_repeats(s):
  for i in range(2,len(s)+1):
    if s[:i]*(len(s)//i) == s:
      return len(s)//i

