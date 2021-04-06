
import datetime
​
def has_friday_13(month, year):
​
  # Local variable 
  day = 13
  
  # Store the date of inside variable 
  date = datetime.datetime(year, month, day)
  
  # Get the day and store in variable 
  week_day = date.strftime("%A")
  
  # Check if weekday is a 'Friday'
  if week_day == 'Friday':
    # Return true
    return True
    
  # Return false
  return False

