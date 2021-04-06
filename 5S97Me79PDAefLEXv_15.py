
import re
def lambda_to_def(code):
  meh = re.match(r'(.*) = lambda (.*?):(.*)', code)
  
  return 'def {}({}):\n\treturn{}'.format(meh.group(1),meh.group(2),meh.group(3))

