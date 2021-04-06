
import re
def tweet(txt):
  pattern = "@[a-zA-Z]+|#[a-zA-Z]+"
  l = re.findall(pattern, txt)
  return " ".join(l)

