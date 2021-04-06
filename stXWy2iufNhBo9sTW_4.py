
def valid_rondo(s):
  n = len(s)
  return list(s) == [chr(66+i//2) if i%2 else 'A' for i in range(n)] and n%2==1 and n!=1

