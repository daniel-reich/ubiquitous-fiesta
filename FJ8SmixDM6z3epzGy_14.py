
def check_perfect(number):
  
  # Local variables 
  count = 0
  sum = 0
  
  # Loop from 0 to number 
  for i in range(0, number):
    # Increase the count by one 
    count += 1
    
    # Check if count is a factor of number 
    if number % count == 0 and count != number:
      # Sum up the count and store in variable 
      sum += count
  
  # Check if sum is equal to number 
  if sum == number:
    # Return true 
    return True
  
  # Return false 
  return False

