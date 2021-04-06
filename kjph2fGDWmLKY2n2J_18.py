
import re
​
def valid_color (color):
  if re.search("^rgba", color) != None:
    if re.search("^rgba\(\s?(0?\.?\d*\s?,\s?){3}0?\.?\d*\s?\)$", color) != None:
      return True
    
  elif re.search("^rgb", color) != None:
    if re.search("^rgb\(\s?((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[0-9][0-9]|[0-9])\s?,\s?){2}(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[0-9][0-9]|[0-9])\s?\)$", color) != None:
      return True
      
    elif re.search("^rgb\(\s?((100|[0-9][0-9]|[0-9])%\s?,\s?){2}(100|[0-9][0-9]|[0-9])%\s?\)$", color) != None:
      return True
      
  return False

