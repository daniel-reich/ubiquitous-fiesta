
def is_zygodrome(num):
  s = str(num)
  def is_zygstr(s):
    e = s[0] 
    if len(s) > 1 and s[0] == s[1]:
      while s and s[0] == e:
        s = s[1:]
      return is_zygodrome(s) if s else True
    return False
  return is_zygstr(s)

