
def generate_palindromes(l):
  return [i for i in range(l+1) if str(i)==str(i)[::-1]][-15:]

