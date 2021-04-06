
import re
​
def edabit_in_string(txt):
  return "NO" if re.search('e.*d.*a.*b.*i.*t', txt) == None else "YES"

