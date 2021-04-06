
import re
def sig_figs(num):
  regex = r"^-?0*\.?0*$"
  if re.match(regex,num):
    return 0
  regex = r"^-?0*([1-9][0-9]*[1-9])0*$"
  if re.match(regex,num):
    return len((re.match(regex,num).group(1)))
  regex = r"^-?0*\.?0*([1-9]\.?[0-9]*\.?[0-9]*)\.?$"
  if re.match(regex,num):
    return len((re.match(regex,num).group(1).replace(".","")))

