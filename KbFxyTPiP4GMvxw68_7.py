
def longest_zero(s):
  for amount in range(len(s),0,-1):
    if "0" * amount in s:
      return "0" * amount
  return ""

