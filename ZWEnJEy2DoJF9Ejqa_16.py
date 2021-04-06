
import re
def edabit_in_string(txt):
  return ['NO', 'YES'][bool(re.match('.*e.*d.*a.*b.*i.*t.*', txt))]

