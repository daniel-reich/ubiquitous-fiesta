
import re
def negative_sum(chars):
  return sum(map(int, re.findall(r"-\d+", chars)))

