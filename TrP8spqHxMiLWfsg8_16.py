
class Node:
  def __init__(self,data):
    self.data = data
    self.left = None
    self.right = None
    self.tree = [data]
  def insert(self,data):
    node = Node(data)
    if data < self.data:
      if not self.left:
        self.left = node
      else:
        self.left.insert(data)
    elif not self.right:
      self.right = node
    else:
      self.right.insert(data)
    self.tree.append(data)
  def PrintTree(self):
    return sorted(self.tree)

