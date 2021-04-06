
from collections import OrderedDict
​
def clean_up(files, sort):
  folders = OrderedDict()
  for f in files:
    p_s = f.split('.')
    key = p_s[0 if sort == 'prefix' else 1]
    if key not in folders.keys():
      folders[key] = []
    folders[key].append(f)
  
  folders_list = []
  for v in folders.values():
    folders_list.append(v)
  return folders_list

