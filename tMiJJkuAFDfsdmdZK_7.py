
import re
​
def to_snake_case(string):
  return re.sub(r"([A-Z])" , lambda m : "_" + m.group().lower() , string);
​
def to_camel_case(string):
  return re.sub(r"_([a-zA-Z])" , lambda m : m.group(1).upper() , string);

