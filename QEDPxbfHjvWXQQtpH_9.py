
def count_palindromes(num1, num2):
  ct=0
  for x in range(num1, num2+1):
    str1=str(x)
    if str1 == str1[::-1]:
      ct+=1
  return ct

