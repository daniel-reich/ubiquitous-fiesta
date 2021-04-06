
def valid_rondo(s):
  A=s[1:-1].split('A')
  return s[0]==s[-1]=='A' and A[0]=='B' and A==sorted(A)

