
import re
def validate_email(txt):
  val=re.search("\w+@\w+\.\w+",txt)
  return True if val else False

