
import re
​
def split_n_cases(string, cases):
  portions = len(string) / cases
  return (re.findall('.{{{}}}'.format(int(portions)), string)
    if portions.is_integer() else ['Error'])

