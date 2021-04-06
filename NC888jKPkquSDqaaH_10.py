
from collections import OrderedDict
​
def clean_up(files, sort):
  if sort == 'prefix':
    return clean_prefix(files)
  return clean_suffix(files)
  
def clean_prefix(files):
  cleaned = OrderedDict()
  for file in files:
    prefix, _ = file.split('.')
    if prefix in cleaned:
      cleaned[prefix].append(file)
    else:
      cleaned[prefix] = [file]
  return list(cleaned.values())
  
def clean_suffix(files):
  cleaned = OrderedDict()
  for file in files:
    _, suffix = file.split('.')
    if suffix in cleaned:
      cleaned[suffix].append(file)
    else:
      cleaned[suffix] = [file]
  return list(cleaned.values())

