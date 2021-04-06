
import re
def switcheroo(txt):
  return re.sub('_','',re.sub(r'nts(?=\b)','nce_',re.sub(r'nce(?=\b)','nts_',txt)))

