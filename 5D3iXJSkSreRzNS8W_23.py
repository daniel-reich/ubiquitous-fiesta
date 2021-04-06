
def news_at_ten(t, n):
  return [(' '*n+t+' '*n)[x:n+x] for x in range(n+len(t)+1)]

