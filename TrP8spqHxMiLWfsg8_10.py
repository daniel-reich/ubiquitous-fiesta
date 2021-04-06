
class Node:
  tree=[]
  def __init__(self, data):
    self.left = None
    self.right = None
    self.data = data
    # Hint this line to clear the list for every object
    Node.tree.clear()
  
  def insert(self, data):
    if data<self.data:
      if self.left is None:
        self.left = Node(data)
      else:
        self.left.insert(data)
    else:
      if self.right is None:
        self.right = Node(data)
      else:
        self.right.insert(data)
    
  def PrintTree(self):
    if self.left:
      self.left.PrintTree()
    Node.tree.append(self.data)
    if self.right:
      self.right.PrintTree()
    return Node.tree

