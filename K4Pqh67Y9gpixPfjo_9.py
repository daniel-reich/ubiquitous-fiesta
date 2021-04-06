
import re
​
def is_valid_PIN(pin):
  if len(pin) == 4 or len(pin) == 6:
    return bool(re.match(r'\d+', pin))
  
  return False

