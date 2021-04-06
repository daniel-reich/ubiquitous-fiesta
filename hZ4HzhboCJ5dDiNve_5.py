
def special_reverse_string(txt):
  import re
​
  spaces = [m.start() for m in re.finditer(' ', txt)]
  uppers = [i for i, c in enumerate(txt) if c.isupper()]
​
  result = re.sub(' ', '', txt)[::-1].lower()
  for index in spaces:
      result = result[:index] + ' ' + result[index:]
  return "".join(c.upper() if i in uppers else c for i, c in enumerate(result))

