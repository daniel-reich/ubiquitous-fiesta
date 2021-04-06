
import re
​
def palindromic_date(date):
  groups = re.findall(r"(\d{2})", date)
  return "".join((groups[0], groups[1])) == "".join((groups[2], groups[3]))[::-1] \
    and "".join((groups[1], groups[0])) == "".join((groups[2], groups[3]))[::-1]

