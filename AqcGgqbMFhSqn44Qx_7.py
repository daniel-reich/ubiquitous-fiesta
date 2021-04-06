
import re
def tweet(txt):
  matches = re.findall('[#|@][\w]+', txt)
  return ' '.join(matches)

