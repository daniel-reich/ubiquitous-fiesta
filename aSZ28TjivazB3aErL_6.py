
def letters_only(s):
  if len (s)==0 : return False
  for i in s:
    if i == " " or i.islower():
      continue
    else :
      return False
  return True

