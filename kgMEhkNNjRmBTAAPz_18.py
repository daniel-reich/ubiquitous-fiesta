
import re 
def remove_special_characters(txt):
  final = re.sub(r'[^\s\w_-]+', '', txt)
  return final

