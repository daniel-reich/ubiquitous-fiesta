
import re
​
def validate_relationships(s):
  return eval(re.sub(r'\b=(?=\b|-)', '==', s))

