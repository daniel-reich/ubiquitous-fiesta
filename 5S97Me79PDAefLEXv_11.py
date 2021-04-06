
import re
def lambda_to_def(code):
  p = re.compile( r"^(\w+) = lambda (.+): (.+)$")
  parts = p.match(code).groups()
  #print(parts)
  returned_string = "def " + parts[0] + "(" + parts[1] + "):\n\treturn " + parts[2]
  return returned_string

