
import re
def switcheroo(txt):
  return re.sub('_temp_', 'nce', re.sub('nce\\b', 'nts', re.sub('nts\\b', '_temp_', txt)))

