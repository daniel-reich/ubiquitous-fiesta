
def fauna_number(txt):
  import re
  rx=re.compile(r"(\d+)" # A number
          r"\s"    # A space
          r"(muggercrocodile|one-hornedrhino|python|moth"
          r"|monitorlizard|bengaltiger)" #A word
          ,re.VERBOSE)
​
  d=rx.findall(txt)
  d1=[]
  for (j,k) in d:
    d1.append((k,j))
  return d1

