
def longest_word(s):
  return max([i for i in s.split()], key = len)

