
import re
def pig_latin(txt):
  def pig_it(m):
    w = m.group()
    if w[0] in 'aeiouAEIOU': return w + 'way'
    pw = w[1:] + w[0] + 'ay'
    return pw.title() if w[0].isupper() else pw
    
  return re.sub(r'\b\w+\b', pig_it, txt)

