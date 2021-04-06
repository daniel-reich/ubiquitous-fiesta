
def is_astonishing(num):
  s = str(num)
  for i in range(1, len(s)):
    a, b, pre = int(s[:i]), int(s[i:]), 'AB'
    if a > b:
      a, b, pre = b, a, 'BA'
    if num == (a+b)*(b-a+1)/2:
      return pre+'-Astonishing'
  return False

