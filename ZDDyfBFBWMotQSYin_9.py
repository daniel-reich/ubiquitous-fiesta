
def is_harshad(num):
  ##to check if the number is divisible by the sum of its digits
  ##we need to grab each digit and then add them together
  ##then we can try number mod sum == 0 and return the resulting boolean
  
  ##first we need to grab each digit and sum them together
  ##to do this, we might want to convert the number into a string
  ##then we can do for each letter in string
  ##in this for loop, add the int(letter) to a running total
  
  if num == 0:
    return False
    
  numstr = str(num)
  sum = 0
  for letter in numstr:
    sum += int(letter)
  
  if num%sum == 0:
    return True
  else:
    return False

