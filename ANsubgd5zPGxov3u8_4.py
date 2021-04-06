
import re
def initialize(names):
  return [re.sub("\B\w+",".",x) for x in names]

