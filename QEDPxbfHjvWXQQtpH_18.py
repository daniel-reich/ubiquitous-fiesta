
def count_palindromes(num1, num2):
  count = 0
  for i in range(num1, num2 + 1):
    if str(i) == str(i)[::-1]:
      count += 1
  return count

