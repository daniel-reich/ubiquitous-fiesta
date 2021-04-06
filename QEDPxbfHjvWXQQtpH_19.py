
def count_palindromes(num1, num2):
  arr =[]
  for x in range(num1, num2+1):
    if str(x) == str(x)[::-1]:
      arr.append(x)
  return len(arr)

