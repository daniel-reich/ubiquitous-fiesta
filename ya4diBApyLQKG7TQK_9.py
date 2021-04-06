
import re
def validate_relationships(txt):
  return eval(''.join('==' if i=='=' else i for i in re.findall('[-\d+]+|[<>=]+',txt)))

