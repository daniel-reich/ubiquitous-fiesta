
import re
def assignment(date):
  return True if re.match(r"\b\d{4}\/\d{2}\/\d{2}\b", date)!=None else False

