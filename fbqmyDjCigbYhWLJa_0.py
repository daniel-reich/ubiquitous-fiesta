
import re
​
def split_into_buckets(phrase, n):
  a = re.findall("(?: |^)([a-z ]{1," + str(n) + "})(?= |$)", phrase)
  return [] if " ".join(a) != phrase else a

