
def is_consecutive(s, n=1):
  # recursive code in here
  if n > len(s)//2:
    return False
  asc = "".join(str(int(s[:n])+x) for x in range(len(s)//n)) 
  desc = "".join(str(int(s[:n])-x) for x in range(len(s)//n))
  if asc == s or desc == s:
    return True
  return is_consecutive(s, n+1)

