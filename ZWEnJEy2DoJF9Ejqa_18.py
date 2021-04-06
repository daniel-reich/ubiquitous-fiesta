
import re
​
def edabit_in_string(string):
  return "YES" if re.findall(r"e.*d.*a.*b.*i.*t" , string) else "NO"

