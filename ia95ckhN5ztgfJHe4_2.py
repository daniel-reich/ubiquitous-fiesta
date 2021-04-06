
import re
def comments_correct(txt):
  return bool(re.match(r"^(//|/\*\*/)*$",txt))

