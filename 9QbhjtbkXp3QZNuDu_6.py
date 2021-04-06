
def generate_palindromes(limit):
  palindromes_15 = []
  for i in range(limit,-1,-1):
    if str(i) == str(i)[::-1]: palindromes_15.append(i)
    if len(palindromes_15) == 15: break
    
  return sorted(palindromes_15)

