
import re, datetime
​
def convert(m):
  txt = m.group()
​
  if   txt[2] == "/": fmt = "%d/%m/%y"
  elif txt[2] == ".": fmt = "%d.%m.%y"
  else:               fmt = "%B, %d. %y"
​
  try:
    date = datetime.datetime.strptime(txt, fmt)
    year = date.year - 100 * (date.year > 2024)
    return date.strftime(fmt[:-2]) + str(year)
  except:
    return txt
​
def small_favor(sentence):
  return re.sub(r"\d\d([/.])\d\d\1\d\d|\w+, \d\d\. \d\d", convert, sentence)

