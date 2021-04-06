
def palindrome_type(n):
  def palindrome_check(input_str):
    print("The number is " + input_str + ".")
    start = 0
    end = len(input_str) -1
    num_palindrome = True
    while start <= end:
      if input_str[start] == input_str[end]:
        start += 1 
        end -=1
      else:
        num_palindrome = False
        break
    print("Is number a palindrome, " , num_palindrome , ".")
    return num_palindrome
    
    
    #Checking Decimal
  decimal_check = palindrome_check(str(n))
  bin_number_str = str(bin(n))
  binary_check = palindrome_check(bin_number_str[2:])
  
  
  if decimal_check == True and binary_check == True:
    return "Decimal and binary."
  elif decimal_check == True and binary_check == False:
    return "Decimal only."
  elif decimal_check == False and binary_check == True:
    return "Binary only."
  elif decimal_check == False and binary_check == False:
    return "Neither!"

