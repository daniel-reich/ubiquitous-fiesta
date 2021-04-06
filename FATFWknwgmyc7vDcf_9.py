
import re
​
def replace_year(match):
  date_parts = list(match.groups())
  separator = date_parts[1]
  del date_parts[1]
  
  if int(date_parts[2]) < 25:
    date_parts[2] = "20" + date_parts[2]
  else:
    date_parts[2] = "19" + date_parts[2]
  return separator.join(date_parts)
​
def replace_year_with_month_format(match):
  date_parts = list(match.groups())
  
  if int(date_parts[2]) < 25:
    date_parts[2] = "20" + date_parts[2]
  else:
    date_parts[2] = "19" + date_parts[2]
  return date_parts[0] + ', ' + date_parts[1] + '. ' + date_parts[2] + '.'
​
def small_favor(sentence):
  firstPass = re.sub(r'([0-9]{2})([/.])([0-9]{2})[/.]([0-9]{2})', replace_year, sentence)
  
  return re.sub(r'(January|February|October), ([0-9]{2}). ([0-9]{2}).', replace_year_with_month_format, firstPass)

