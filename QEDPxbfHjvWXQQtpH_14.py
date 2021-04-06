
def count_palindromes(start, end):
  counter = 0
  for num in range(start, end+1):
    if is_palindrome(num):
      counter += 1
  return counter
    
def is_palindrome(num):
  digits = []
  while num > 0:
    digits.append(num%10)
    num //= 10
  return digits == list(reversed(digits))

