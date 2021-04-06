
def letters_only(s):
  if len(s)==0:
    return False
  return all(i.islower() for i in s.split())

