
def longest_zero(s):
  count = 0
  if '0' not in s:
    return ''
  while count < len(s):
    if s[0] == '0':
      count = max(count, s.find('1'))
    try:
      s = s[s.index('1') + 1:]
    except ValueError:
      count = max(len(s), count)
      s = s[s.find('1')]
  return '0' * count

