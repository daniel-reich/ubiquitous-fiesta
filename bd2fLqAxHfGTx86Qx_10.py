
import re
def can_complete(initial, word):
  query = "(.*)".join([ch for ch in initial]) 
  return True if re.match(query, word) else False

