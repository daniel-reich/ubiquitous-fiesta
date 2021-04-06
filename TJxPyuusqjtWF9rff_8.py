
def get_only_evens(n):
  return [n[x] for x in range(0,len(n),2) if not n[x]%2]

