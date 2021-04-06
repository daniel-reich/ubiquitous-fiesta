
class Node:
  final_tree = []
  def __init__(self, data, root=True):
    self.left = None
    self.right= None
    self.data = data
    self.root = root
    if root:
      Node.final_tree = [data]
    
  def insert(self, data):
    if self.root:
      Node.final_tree.append(data)
    if data < self.data:
      if self.left: self.left.insert(data)
      else: self.left = Node(data,False)
    if data > self.data:
      if self.right: self.right.insert(data)
      else: self.right = Node(data,False)
    
  def PrintTree(self):
    return sorted(Node.final_tree)

