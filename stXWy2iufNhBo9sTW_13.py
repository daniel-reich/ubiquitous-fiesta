
def valid_rondo(s):
  if len(s) < 3 or len(s) % 2 == 0: return False
  if set([s[i] for i in range(len(s)) if i%2==0]) != {'A'}: return False
  if ''.join([s[i] for i in range(len(s)) 
  if i%2!=0]) not in 'BCDEFGHIJKLMNOPQRSTUVWXYZ': return False
  return True

