
def generate_palindromes(limit):
  return [x for x in range(10, limit+1) if str(x) == str(x)[::-1]][-15:]

