
def dashed(s):
  return "".join([v, '-' + v + '-'][v in "AEIOUaeiou"] for v in s)

