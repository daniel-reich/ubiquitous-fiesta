
def count_palindromes(num1, num2):
  return len([num for num in range(num1, num2 + 1) if str(num) == str(num)[::-1]])

