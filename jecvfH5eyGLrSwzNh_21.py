
import re
​
def fauna_number(txt):
  animals = [ "muggercrocodile", "one-hornedrhino", "python", 
        "moth", "monitorlizard", "bengaltiger"  ]
  
  return [(y, x) for x, y in re.findall(r'(\d+) ([\w-]+)', txt)
                            if y in animals]

