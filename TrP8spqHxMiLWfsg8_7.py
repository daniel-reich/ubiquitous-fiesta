
class Node:
​
  tree_lst = []
​
  def __init__(self, num):
    self.data = num
    self.left = None
    self.right = None
    self.tree_lst.clear()
​
  def insert(self, num):
    if not self.left and num <= self.data:
      node = Node(num)
      self.left = node
    elif not self.right and num > self.data:
      node = Node(num)
      self.right = node
    elif num <= self.data:
      self.left.insert(num)
    else:
      self.right.insert(num)
​
  def PrintTree(self):
    if self.left:
      self.tree_lst = self.left.PrintTree()
    self.tree_lst.append(self.data)
    if self.right:
      self.tree_lst = self.right.PrintTree()
    return self.tree_lst

