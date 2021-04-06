
def valid_rondo(s):
  A = s[::2] ; sec = s[1::2] ; lets = "BCDEFGHIJKLMNOPQRSTUVWXYZ"
  if s[-1]!= 'A' or len(A)==1: return False
  return all(i=="A" for i in A) and sec in lets

