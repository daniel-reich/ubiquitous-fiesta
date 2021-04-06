
def count_palindromes(num1, num2):
  return sum([1 for n in range(num1, num2+1) if str(n) == str(n)[::-1]])

