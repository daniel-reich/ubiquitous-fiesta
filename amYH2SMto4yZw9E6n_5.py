
import re
​
def validate(s):
  formats = {
    r'\+1-\d{3}-\d{3}-\d{4}',
    r'1-\d{3}-\d{3}-\d{4}',
    r'1\s\(\d{3}\)\s\d{3}-\d{4}',
    r'1\.\d{3}\.\d{3}\.\d{4}',
    r'1\s\d{3}\s\d{3}\s\d{4}',
    r'1?\d{10}',
​
    r'\d{3}-\d{3}-\d{4}',
    r'\(\d{3}\)\s\d{3}-\d{4}',
    r'\d{3}\.\d{3}\.\d{4}',
    r'1/\d{3}/\d{3}/\d{4}',
    r'\d{3}/\d{3}/\d{4}',
    r'\d{3}\s\d{3}\s\d{4}'
  }
​
  return any(re.match(f, s) for f in formats)

