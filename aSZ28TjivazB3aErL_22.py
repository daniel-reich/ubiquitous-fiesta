
def letters_only(s):
  letters = "abcdefghijklmnopqrstuvwxyz"
  if len(s)==0:
    return False
  for char in s:
    if char not in letters and char != " ":
      return False
  return True

