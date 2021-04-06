
def plant_trees(w, l, g):
  g+=1
  trees = 0
  cur = 0
  perimeter = (w*2)+((l-2)*2)
  while cur<perimeter:
    if cur+g>perimeter:
      return 0
    cur+=g
    trees+=1
  return trees

