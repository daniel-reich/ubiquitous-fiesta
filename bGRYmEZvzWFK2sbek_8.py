
def get_missing_letters(s):
  ret = ""
  for i in range(97, 123):
    if not chr(i) in s:
      ret = ret + chr(i)
  return ret

