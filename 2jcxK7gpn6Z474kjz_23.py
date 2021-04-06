
import re
def security(txt):
  if re.search('Tx*\$|\$x*T',txt):
    return 'ALARM!'
  return 'Safe'

