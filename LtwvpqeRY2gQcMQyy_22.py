
import re
def sig_figs(num):
  try:
    if num[0] == "-" or num[0] == "0":
      num = re.sub(r'^[-0]+','',num)
    if num[0] == ".":
      num = re.sub(r'^[0\.]+','',num)
    elif not "." in num:
      if num[-1] == "0":
        num = re.sub(r'0+\b','',num)
    num = re.sub(r'\D','',num)
    return len(num)
  except IndexError:
    return 0

