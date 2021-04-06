
import re
​
def markdown(symb):
  def makdownify(sentence, word):
    find = r'({}[!?.]*)'.format(word) 
    sub = r'{symb}\1{symb}'.format(symb=symb)
    return re.sub(find, sub, sentence, flags=re.IGNORECASE)
  return makdownify

