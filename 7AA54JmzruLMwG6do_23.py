
import re
​
def is_icecream_sandwich(candidate):
  ice_cream_patten = re.compile(r"((.)\2*)");
  slices  = [mtches[0] for mtches in ice_cream_patten.findall(candidate)]
  print(candidate);
  print(slices);
  return len(slices) == 3 and slices[0] == slices[2] and slices[0] != slices[1]

