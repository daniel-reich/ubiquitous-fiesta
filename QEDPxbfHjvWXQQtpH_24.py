
def count_palindromes(num1, num2):
  return len([i for i in range(num1, num2+1) if str(i)[::-1] == str(i)])

