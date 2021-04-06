
def count_palindromes(num1, num2):
  palindromes = []
  for i in range(num1, num2 + 1):
    if len(str(i)) == 1:
      palindromes.append(i)
    elif len(str(i)) == 2 or len(str(i)) == 3:
      if str(i)[0] == str(i)[-1]:
        palindromes.append(i)
    elif len(str(i)) == 4:
      if (str(i)[0] == str(i)[-1]) and (str(i)[1] == str(i)[-2]):
        palindromes.append(i)
    
      
  return len(palindromes)

