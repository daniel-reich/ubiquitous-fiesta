
def palindrome_type(n):
  binaryn = bin(n)[2:]
  i = 0
  while i < len(str(n)) / 2:
    if not str(n)[i] == str(n)[-(i+1)]: 
      n_palindrome = False
      break
    i += 1
    n_palindrome = True
  j = 0
  while j < len(binaryn) / 2:
    if not binaryn[j] == binaryn[-(j+1)]:
      binaryn_palindrome = False
      break
    j += 1
    binaryn_palindrome = True
  if n_palindrome == True and binaryn_palindrome == True:
    return "Decimal and binary."
  if n_palindrome == True and binaryn_palindrome == False:
    return "Decimal only."    
  if n_palindrome == False and binaryn_palindrome == True:
    return "Binary only."
  if n_palindrome == False and binaryn_palindrome == False:
    return "Neither!"

