
def longest_zero(s):
  return ''.join('0' * max(len(el) for el in s.split('1')))

