
import re
def ing_extractor(string):
    return [w for w in string.split() if \
      re.match(r'^\w*?[aeiou\*]+?\w*?ing$', w, flags=re.I)]

