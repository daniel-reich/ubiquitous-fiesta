
class Node:
  def __init__(self, data):
    self.left = None
    self.right = None
    self.data = data
​
  def insert(self, data):
    if data > self.data:
      if self.right == None:
        self.right = Node(data)
      else:
        self.right.insert(data)
    if data < self.data:
      if self.left == None:
        self.left = Node(data)
      else:
        self.left.insert(data)
​
  def PrintTree(self):
    nodevals = []
    if self.left:
      nodevals = nodevals + self.left.PrintTree()
    nodevals = nodevals + [ self.data ]
    if self.right:
      nodevals = nodevals + self.right.PrintTree()
    return nodevals

