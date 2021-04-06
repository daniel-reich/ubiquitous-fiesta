
def generate_palindromes(limit):
  res = []
  for k in range(limit, 0, -1):
    if str(k) == str(k)[::-1]:
      res.append(k)
  return res[::-1][-15:]

