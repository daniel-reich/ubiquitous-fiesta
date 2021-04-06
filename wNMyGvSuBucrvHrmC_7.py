
def number_of_repeats(s):
  return s.count(s[:s[2:].find(s[0])+2])

