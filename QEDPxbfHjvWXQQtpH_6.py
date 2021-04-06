
def count_palindromes(num1, num2):
  return len([x for x in range(num1, num2+1) if str(x)==str(x)[::-1]])

