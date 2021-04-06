
def longest_zero(s):
  for i in range(s.count('0'),0,-1):
    if '0'*i in s:
      return '0'*i

