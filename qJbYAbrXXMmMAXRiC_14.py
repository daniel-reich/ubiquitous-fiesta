
import re
def variable_valid(var):
   if re.search(r"^[\D][\w]+$",var)==None:
    return False
   else:
    return True

