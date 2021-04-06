
class Tree_Box:
  class Tree:
​
    def __init__(self, gap, ident):
      self.g = gap
      self.id = ident
      self.tree = False
    
    def can_plant(self, trees):
      
      need_clear = [ident for ident in list(range(self.id - self.g, self.id + self.g + 1)) if ident in trees.keys()]
​
      for ident in need_clear:
        if trees[ident].tree == True:
          return False
      
      self.tree = True
      return True
​
    def spaces_btn(self, other):
      return abs(self.id - other.id)
​
  def __init__(self, width, length, tree_gap):
    self.w = width
    self.l = length
    self.tg = tree_gap
​
    num_of_trees = self.w + (self.l - 1) + (self.w - 1) + (self.l - 2)
    
    self.trees = {n: Tree_Box.Tree(self.tg, n) for n in range(num_of_trees)}
  
  def plant_trees(self):
    if self.tg > max(self.trees.keys()):
      return False
    for tree in self.trees.keys():
      tree = self.trees[tree]
      tree.can_plant(self.trees)
    return True
  
  def list_trees(self):
    return [tree for tree in self.trees.keys() if self.trees[tree].tree == True]
  
  def symmetry_check(self):
    trees = self.list_trees()
    try:
      return len(list(set([self.trees[trees[n]].spaces_btn(self.trees[trees[n+1]]) for n in range(len(trees) - 1)] + [abs(self.trees[trees[-1]].id - (max(self.trees.keys()) + 1))])) )== 1
    except IndexError:
      return False
​
  def count_trees(self):
    return len(self.list_trees())
​
def plant_trees(w, l, g):
​
  tb = Tree_Box(w, l, g)
​
  tb.plant_trees()
  
  return [tb.count_trees(), 0][tb.symmetry_check() == False]

