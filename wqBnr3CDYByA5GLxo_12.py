
import re
​
def unravel(txt):
  output = [""]
  while True:
    res = re.split("(\[[^\]]+\])", txt, 1)
    output = [pos + res[0] for pos in output]
    if len(res) == 1:
      break
    choices = re.split("\|", res[1][1:-1])
    output = [pos + choice for pos in output for choice in choices]
    txt = res[2]
  output.sort()
  return output

