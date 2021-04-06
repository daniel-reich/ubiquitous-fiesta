
def switches(n):
  if n==1:return 1
  if n%2==0: return 2* switches(n-1)
  return 2* switches(n-1)+1

