
import re
def edabit_in_string(txt):
  booleans = {True:"YES",False:"NO"}
  return booleans[bool(re.search(r'.*e.*d.*a.*b.*i.*t.*',txt))]

