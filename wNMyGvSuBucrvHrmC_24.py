
def number_of_repeats(s):
  for i in range(2,len(s)+1):
    if s[:i]*s.count(s[:i])==s:
      return s.count(s[:i])

