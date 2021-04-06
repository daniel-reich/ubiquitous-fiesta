
import re
def valid_name(name):
  return True if re.match(r'^(([A-Z]{1}\. ){1,2}|([A-Z]{1}[a-z]+ ){1,2}|([A-Z]{1}[a-z]+ [A-Z]{1}\. ))([A-Z]{1}[a-z]+)$', name) else False

