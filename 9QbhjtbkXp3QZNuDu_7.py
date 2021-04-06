
def is_palindrome(n):
  return str(n) == str(n)[::-1]
​
def generate_palindromes(limit):
  
  palindromes = []
  for i in range(0,limit+1):
    if is_palindrome(i):
      palindromes.append(i)
  
  return sorted(palindromes[::-1][:15])

