
def count_palindromes(num1, num2):
  count = 0
  for n in range(num1,num2+1):
    _ = str(n)
    if _ == _[::-1]:
      count += 1
  return count

