
def add_bill(money):
  # Input is a string and we need list of all the entries split by comma
  money = money.split(",")
  # Output sum of dollars in money, initialize with zero
  dollar_total = 0
  # Given
  dollar_string = "d"
  thousand_string = "k"
  
  #Setup variables
  convert = 0
  
  # Loop through every entry
  for entry in money:
    # If entry stars with dollar string use it
    if(entry[0] == dollar_string):
      # Check if entry has thousand string in it
      if(thousand_string in entry[1:]):
        # Convert rest of entry except last character to string
        convert = int(entry[1:-1])
        # Multiply by 1000 and Add conversion to dollar_total
        dollar_total += convert * 1000
      else:
        # Convert rest of entry to string into a number 
        convert = int(entry[1:])
        # Add conversion to total
        dollar_total += convert
  
  # Return the output, in our case dollar_total
  return dollar_total

