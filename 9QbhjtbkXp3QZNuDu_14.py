
def generate_palindromes(limit):
  return [i for i in range(1,limit+1) if str(i) == str(i)[::-1]][-15:]

