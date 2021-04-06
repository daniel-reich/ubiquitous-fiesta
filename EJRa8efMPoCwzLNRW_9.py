
import re
from operator import itemgetter
​
def dakiti(sentence: str) -> str:
  result = []
  chorus = re.findall(r'\b(\S*)(\d{1,2})(\S*)\b', sentence)
  for prefix, i, suffix in sorted(chorus, key=itemgetter(1)):
    result.append('{}{}'.format(prefix, suffix))
  return ' '.join(result)

