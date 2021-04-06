
def generate_palindromes(limit):
  return [n for n in range(limit+1) if str(n) == str(n)[::-1] and n > 9][-15:]

