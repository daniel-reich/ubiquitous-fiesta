
def valid_rondo(s):
  n = s.replace("A","")
  return len(n) and s[::len(s)-1]=="AA" and "AA" not in n and n in "BCDEFGHIJKLMNOPQRSTUVWXYZ"

