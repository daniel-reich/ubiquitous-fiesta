
from os.path import splitext
def clean_up(files, sort):
  d = {}
  i = 0
  for file in files:
    method = splitext(file)[sort == 'suffix']
    if method not in d:
      d[method] = {'i' : i, 'file' : [file]}
      i += 1
    else:
      d[method]['file'].append(file)
  return [x['file'] for x in sorted(d.values(), key = lambda x:x['i'])]

