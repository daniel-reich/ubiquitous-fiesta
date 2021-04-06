
class Node:
  tree=[]
​
  def __init__(self, data):
    self.left = None
    self.right = None
    self.data = data
    # Hint this line to clear the list for every object
    # Node.tree.clear()
    
  def insert(self, data):
    print(data)
    start = self
    while True:
      if data > start.data:
        if start.right is None:
          start.right = Node(data)
          break
        else:
          start = start.right
      else:
        if start.left is None:
          start.left = Node(data)
          break
        else:
          start = start.left
​
  def PrintTree(self):
    if self.left is None:
      if self.right is None:
        return [self.data]
      else:
        return [self.data] + (self.right).PrintTree()
    else:
      if self.right is None:
        return (self.left).PrintTree() + [self.data]
      else:
        return (self.left).PrintTree() + [self.data] + (self.right).PrintTree()

