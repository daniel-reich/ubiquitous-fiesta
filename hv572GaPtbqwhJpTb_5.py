
def elasticize(word):
  n=len(word)
  if n%2:
    pivot=word[n//2]
    left=''
    right=''
    for i in range(n//2):
      left+=word[:n//2][i]*(i+1)
      right+=word[n//2+1:][::-1][i]*(i+1)
    return left+pivot*(n//2+1)+right[::-1]
  else:
    left=''
    right=''
    for i in range(n//2):
      left+=word[:n//2][i]*(i+1)
      right+=word[n//2:][::-1][i]*(i+1)
    return left+right[::-1]

