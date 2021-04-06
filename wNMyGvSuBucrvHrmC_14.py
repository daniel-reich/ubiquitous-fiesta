
def number_of_repeats(s):
  return max([s.count(s[:i]) for i in range(2,len(s))])

