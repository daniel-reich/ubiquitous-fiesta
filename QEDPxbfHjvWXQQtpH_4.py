
def count_palindromes(num1, num2):
  return sum([str(x)==str(x)[::-1] for x in range(num1,num2+1)])

