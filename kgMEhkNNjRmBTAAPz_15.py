
import re
def remove_special_characters(txt):
  return re.sub('[^A-Za-z0-9_\-\ ]+', '', txt)

