
import re
def get_name(address):
  return re.sub('[^a-zA-Z]', '', address[0:address.rfind('@')])

