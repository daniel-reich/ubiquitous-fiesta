
import re
​
def camel_to_snake(string):
  return re.sub(
    '[A-Z]', 
    lambda m: '_' + m.group().lower(), 
    string
  )

