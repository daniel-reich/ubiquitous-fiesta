
import re
def is_zygodrome(num):
  return bool(re.match(r"^(?:(\d)\1+)+$", str(num)))

