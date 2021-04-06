
import re
​
​
def letters_only(s):
  return bool(
    re.search(r'^[a-z ]+$', s)
  )

