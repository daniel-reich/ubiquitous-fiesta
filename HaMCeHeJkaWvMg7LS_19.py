
import re
def sun_loungers(beach):
  return sum(map(lambda z: (len(z)-1)//2, re.findall("(?<=1)0{3,}(?=1)", '10'+beach+'01')))

