
def news_at_ten(t,n):
  t=' '*n+t+' '*n
  return[t[i:n+i]for i in range(len(t)-n+1)]

