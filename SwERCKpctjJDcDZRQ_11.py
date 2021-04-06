
def longest_string(str1, str2):
  s = str1 + str2
  lst = sorted(set(l for l in s))
  return ''.join(lst)

