
def palindrome_type(n):
  decimal = list(str(n)) == list(str(n))[::-1] # assess whether the number is the same read forward and backward
  binary = list(str(bin(n)))[2:] == list(str(bin(n)))[2:][::-1] # assess whether the binary form of the number is the same read forward and backward
​
  if((decimal) and (binary)): # if both decimal and binary forms of the number are palindromes
    return "Decimal and binary."
​
  if(decimal): # if only the decimal form of the number is a palindrome
    return "Decimal only."
​
  if(binary): # if only the binary form of the number is a palindrome
    return "Binary only."
​
  return "Neither!" # if neither forms of the number are palindromes

