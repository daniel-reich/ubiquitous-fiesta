
import re
​
def parse_code(txt):
  return dict(zip(('first_name', 'last_name', 'id'), re.split('0+', txt)))

