
def happiness_number(s):
  count = 0
  while len(s) > 1:
    if ":)" in s[0:2] or "(:" in s[0:2]:
      count += 1
    elif ":(" in s[0:2] or "):" in s[0:2]:
      count -= 1
    s = s[1:]
  return count

