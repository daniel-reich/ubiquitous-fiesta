
import re
​
def best_friend(txt, a, b):
  return not bool(re.search("{}([^{}]|$)".format(a, b), txt))

