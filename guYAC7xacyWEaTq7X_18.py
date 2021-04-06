
def is_autobiographical(n):
  string = str(n)
  for i,char in enumerate(string):
    if string.count(str(i)) != int(char):
      return False
  return True

