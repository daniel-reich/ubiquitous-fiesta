
def valid_rondo(s):
  letters = "BCDEFGHIJKLMNOPQRSTUVWXYZ"
  t = s.replace("A", "")
  return len(s)>=3 and s[0]==s[-1]=="A" and letters[:len(t)]==t

