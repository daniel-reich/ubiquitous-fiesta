
import re 
def deep_sum(lst):
  return sum(deep_sum(w) if type(w) == list else sum(map(int,re.findall(r'\-?\d+',w))) for w in lst)

