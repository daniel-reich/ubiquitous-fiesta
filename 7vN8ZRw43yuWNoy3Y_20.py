
import re
def parse_code(txt):
  pattern = re.compile(r'([a-zA-Z]+)\d+([a-zA-Z]+)0+(\d*)')
  result = pattern.fullmatch(txt)
  student = {
    "first_name": result.group(1),
    "last_name": result.group(2),
     "id": result.group(3)
  }
  return student

