
import re
def to_snake_case(txt):
  return ''.join(i if i.islower() else '_'+i.lower() for i in txt)
def to_camel_case(txt):
  return ''.join([txt.split('_')[0]]+[i.capitalize() for i in txt.split('_')[1:]]) if len(txt.split('_'))-1 else txt

