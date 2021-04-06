
from itertools import chain
​
def search_folders(folders, ancestor, F):
  if ancestor == F: return [F]
  if not ancestor in folders.keys(): return []
  for child in folders[ancestor]:
    path = search_folders(folders, child, F)
    if len(path):
      return [ancestor] + path
  return []
​
def last_ancestor(folders, X, Y):
  if X == Y: return X
  # find root - any folder which is not a child of another folder
  root = list(set(folders.keys()) - set(chain.from_iterable(folders.values())))[0]
  # search tree for path to X
  Xpath = ''.join(search_folders(folders, root, X))
  # search tree for path to Y
  Ypath = ''.join(search_folders(folders, root, Y))
  # compare pathX with pathY and return last common folder
  for i in range(min(len(Xpath), len(Ypath))):
    if Xpath[i] != Ypath[i]:
      i -= 1
      break
  return Xpath[i]

