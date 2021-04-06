
import re
def small_favor(sentence):
  p = re.compile(r'(?<=\.|/)\d{2}(?= |$)|(?<=January, \d{2}. )\d{2}(?=. |.$)|(?<=February, \d{2}. )\d{2}(?=. |.$)|(?<=October, \d{2}. )\d{2}(?=. |.$)')
  s = sentence
  for i in range(len(p.findall(sentence))):
    dec = p.findall(s)[0]
    cen = '20' if int(dec)<25 else '19'
    s = re.sub(p, cen + dec, s, 1)
  return s

