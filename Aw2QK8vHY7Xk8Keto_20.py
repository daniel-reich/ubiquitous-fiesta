
def longest_word(s):
  return max((w for w in s.split()),key=len)

