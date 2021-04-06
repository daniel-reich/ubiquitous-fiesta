
def generate_palindromes(limit):
  res = []
  for x in range(limit,1,-1):
    if str(x)==str(x)[::-1]:
      res.append(x)
    if len(res)==15:
      break
  return sorted(res)

