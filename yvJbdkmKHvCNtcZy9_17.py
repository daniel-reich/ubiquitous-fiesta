
def is_disarium(number):
  
  # Local variables 
  position = 0
  product = 1
  sum = 0
  
  # Turn number into string and store in variable 
  number = str(number)
  
  # Loop through the number 
  for digit in number:
    # Increase value of position by one 
    position += 1
    
    # Get the number and turn to integer 
    digit = int(digit)
    
    # Loop from 0 to position 
    for i in range(0, position):
      # Get the product and store in variable 
      product *= digit
    
    # Sum up the product
    sum += product 
    
    # Reset the value of product to one 
    product = 1
  
  # Turn number back to integer 
  number = int(number)
  
  # Check if sum equals number 
  if sum == number:
    # Return true 
    return True
  
  # Return false 
  return False

