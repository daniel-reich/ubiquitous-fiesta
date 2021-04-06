
import re
def is_valid_phone_number(txt):
  find = re.findall('\(\d{3}\) \d{3}-\d{4}', txt)
  return True if (find == [txt]) and len(find) != 0 else False

