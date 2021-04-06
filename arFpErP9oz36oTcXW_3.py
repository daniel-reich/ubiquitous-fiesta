
import re
def secret(txt):
  return re.sub("(\w+)(?= ) (.*)", r"<\1 class='\2'></\1>", txt.replace('.',' '))

