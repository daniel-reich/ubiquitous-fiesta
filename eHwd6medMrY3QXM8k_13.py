
def is_consecutive(s):
  for n in range(1, len(s)//2+1):
    asc = "".join(str(int(s[:n])+x) for x in range(len(s)//n)) 
    desc = "".join(str(int(s[:n])-x) for x in range(len(s)//n))
    if asc == s or desc == s:
      return True
  return False

