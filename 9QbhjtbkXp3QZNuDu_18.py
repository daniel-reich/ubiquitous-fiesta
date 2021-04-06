
def generate_palindromes(limit):
  A=[]
  for i in range(10, limit+1):
    if str(i)==str(i)[::-1]:
      A.append(i)
  return A[-15:]

