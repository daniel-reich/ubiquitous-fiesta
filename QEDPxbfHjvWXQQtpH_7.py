
def count_palindromes(num1, num2):
  res = 0
  for x in range(num1,num2+1):  
    if str(x) == str(x)[::-1]:
      res +=1
  return res

