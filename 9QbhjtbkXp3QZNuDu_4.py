
def generate_palindromes(limit):
  is_pal = lambda n: str(n) == str(n)[::-1]
  ans = []
  while len(ans)<15:
    if is_pal(limit): ans = [limit] + ans
    limit-=1
  return ans

