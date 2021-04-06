
from pathlib import PurePath
​
def get_filename(path):
  return PurePath(path).name

