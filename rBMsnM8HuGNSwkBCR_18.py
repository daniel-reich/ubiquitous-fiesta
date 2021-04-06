
import re
def add_bill(money):
  money = re.findall(r'd\d+k?',money)
  dollars = list(map(lambda x: re.sub(r'd','',x),money))
  dollars = list(map(lambda x: re.sub(r'k','000',x),dollars))
  return sum(list(map(lambda x: int(x),dollars)))

