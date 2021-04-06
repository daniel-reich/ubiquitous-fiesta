
def longest_string(str1, str2):
  res = str1 + str2
  res = sorted(list(set([ch for ch in res])))
  return "".join(res)

