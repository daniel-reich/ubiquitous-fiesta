
import re
​
​
def validate_relationships(txt):
  return eval(re.sub('(\d)=', r'\1==', txt))

