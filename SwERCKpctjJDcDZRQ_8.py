
def longest_string(str1, str2):
  c = str1+str2
  c = set(c)
  return "".join([i for i in sorted(c)])

