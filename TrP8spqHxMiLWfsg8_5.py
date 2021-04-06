
class Node:
  def __init__(self, data):
    self.left = None
    self.right = None
    self.data = data
​
  def insert(self, data):
    if data <= self.data:
      if isinstance(self.left, Node):
        self.left.insert(data)
      else:
        self.left = Node(data)
    elif isinstance(self.right, Node):
      self.right.insert(data)
    else:
      self.right = Node(data)
      
  
  def PrintTree(self):
    result = []
    if isinstance(self.left, Node):
      result += self.left.PrintTree()
    result.append(self.data)
    if isinstance(self.right, Node):
      result += self.right.PrintTree()
    return result

