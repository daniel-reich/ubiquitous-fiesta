
def remove_leading_trailing(n):
  try:n=str(int(n))
  except:
    n=n.rstrip('0');
    n=str((int(n[:-1]))if n[-1]=='.'else float(n))
  return n

