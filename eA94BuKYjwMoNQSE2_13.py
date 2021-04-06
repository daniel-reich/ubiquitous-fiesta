
def correct_signs(txt):
  chars = txt.split(" ")
  for i in range(2, len(chars), 2):
    if chars[i-1] == ">":
      if not(int(chars[i-2]) > int(chars[i])):
        return False
    elif not(int(chars[i-2]) < int(chars[i])):
      return False
  return True

