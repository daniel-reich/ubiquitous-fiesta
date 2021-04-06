
import re
​
def is_valid_phone_number(txt):
  print(txt)
  txt_match=re.match("\(\d{3}\) \d{3}-\d{4}",txt,re.I)
  if txt_match:
    print(str(txt_match.group()))
    return(txt_match.group()==txt)
  else:
    return(False)

