
import re
def small_favor(sentence):
  def year(y):
    return '20' + y if int(y) < 25 else '19' + y
  p1 = '\d{2}\.\s'
  p2 = '\d{2}(?:\.|\/)\d{2}(?:\.|\/)'
  if not "Fakemonthy" in sentence:
    return re.sub(r'({}|{})(\d\d)'.format(p1,p2),lambda x: x.group(1) + year(x.group(2)),sentence)
  return sentence

