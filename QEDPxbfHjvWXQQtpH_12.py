
def count_palindromes(num1, num2):
  count = 0
  while num1 <= num2:
    if str(num1)[::-1] == str(num1):
      count += 1
    num1 += 1
  return count

