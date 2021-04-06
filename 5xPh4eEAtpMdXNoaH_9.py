
def longest_palindrome(s):
  res = {}
  for i in range(len(s)):
    item = s[i]
    if item in res:
      res[item] += 1
    else:
      res[item] = 1
  uniques = len([i for i in list(res.values()) if i % 2])
  return len(s) if uniques <= 1 else len(s) - uniques + 1

