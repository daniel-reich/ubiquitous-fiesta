
import re
def is_valid_phone_number(txt):
  return bool(re.fullmatch(r"\(\d{3}\) \d{3}-\d{4}", txt))

