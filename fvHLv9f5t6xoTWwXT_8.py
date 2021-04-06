
def grab_number_sum(s):
  import re
  return sum(list(map(int,re.findall(r"\d+",s))))

