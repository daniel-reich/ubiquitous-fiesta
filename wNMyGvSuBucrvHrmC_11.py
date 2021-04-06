
def number_of_repeats(s):
  for i in range(len(s)):
    if s.count(s[:i]) > 1 and s[:i] != '':
      return s.count(s[:i])
  return 1

