
import re
​
def domino_chain(dominos):
  return re.sub(
    '^[^ //]*', 
    lambda match: '/' * len(match.group()),
    dominos,
  )

