
def get_missing_letters(s):
  all = "abcdefghijklmnopqrstuvwxyz"
  ans = ""
  for c in all:
    if(c not in s):
      ans += c
  return ans

