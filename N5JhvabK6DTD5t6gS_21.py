
import re
def markdown(symb):
  def format_string(sentence,match):
    return re.sub('\S+', lambda x: '{0}{1}{0}'.format(symb,x.group(0)) if ''.join(re.findall('[A-Za-z]',x.group(0))).lower() == match.lower() else x.group(0), sentence)
  return format_string

