
import re
def get_prices(lst):
  answer =[]
  for item in lst:
    answer.append(float(''.join(re.findall("\d+.\d\d",item))))
  return answer

